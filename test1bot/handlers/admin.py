from curses.ascii import FS
from time import time
from aiogram.dispatcher import FSMContext   # can be used for more simply getting data from the storage.
from aiogram.dispatcher.filters.state import State, StatesGroup 
from create_bot import dp, bot
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from database import sqlite_db
from keyboards import admin_kb
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup    # инлайн кнопка и инлайн клавиатура, которая появляется рядом с сообщение к которому она принадлежит
from config import *

ID = None

""" Function for sending the message to admin that bot started """
async def send_to_admin_launch(dp):
    await bot.send_message(chat_id=admin_id, text='Bot started')


""" Создание машины состояний  """
class FSMAdmin(StatesGroup):

    # фактически я буду добавлять определенные значения к этим атрибутам класса 
    photo = State()
    name = State()
    descripption = State()
    price = State()


# Проверка юзера на админа
# @dp.message_handler(comands=['moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message):

    global ID 
    ID = message.from_user.id

    await bot.send_message(message.from_user.id, 'Что надо, хозян?', reply_markup=admin_kb.button_case_admin)
    await message.delete()


# base handler that start this machine of states
# admin type Загрузить and get reply
#@dp.message_handler(commands='Загрузить', store=None)
async def cm_start(message : types.Message):
    
    if message.from_user.id == ID:

        await FSMAdmin.photo.set()
        await message.reply('Загрузи фото')


# выход из состояния
# state="*" - обозначает, что выход может быть из любого состояния
#@dp.message_handler(state="*", commands='Отмена')
#@dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):

    if message.from_user.id == ID:

        current_state = await state.get_state()     # getting current state with method get_state
        
        if current_state is None:
            return
        # если бот находится в каком-либо состоянии 
        await state.finish()
        await message.reply('OK')


# handler that get reply from user
# state=FSMAdmin.photo - bot understand that precisely come into first handler
#@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):

    if message.from_user.id == ID:

        async with state.proxy() as data:

            data['photo'] = message.photo[0].file_id

        await FSMAdmin.next()       # переводим бота в ожидание следующего ответа
        await message.reply('Теперь введи название')


# second handler that get reply from user
#@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):

    if message.from_user.id == ID:

        async with state.proxy() as data:       # open dictionary that storage information like data

            data['name'] = message.text

        await FSMAdmin.next()       # переводим бота в ожидание следующего ответа
        await message.reply('Введите описание')


# thirst handler that get reply from user
#@dp.message_handler(state=FSMAdmin.descripption)
async def load_description(message: types.Message, state: FSMContext):

    if message.from_user.id == ID:

        async with state.proxy() as data:       # open dictionary that storage information like data

            data['description'] = message.text

        await FSMAdmin.next()       # переводим бота в ожидание следующего ответа
        await message.reply('Укажите цену')

# fourth handler that get reply from user
#@dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):

    if message.from_user.id == ID:

        async with state.proxy() as data:       # open dictionary that storage information like data

            data['price'] = float(message.text)

        # async with state.proxy() as data:
        #     await message.reply(str(data))      # будет выводиться значения из словаря   

        await sqlite_db.sql_add_command(state)

        # after this command bot fully clean storage and state doesn't data and ready for new data
        await state.finish()   


""" For inline buttons """
# callback_query_handler - обработчик вызываемого запроса
# callback_query - это придуманное название, тип данных после :
# show_alert - всплывающееся окно после
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):

    await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
    # bot sending to admin a message that specified item was deleted
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена', show_alert=True)


@dp.message_handler(commands='Удалить')
async def delete_item(message: types.Message):

    if message.from_user.id == ID:

        read = await sqlite_db.sql_read2()

        # getting table menu
        for ret in read:

            # bot sending user photo and data about item
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
            # also bot sending with every item one inline button
            await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))


""" Регистрация обработчиков """
def register_handlers_admin(dp : Dispatcher):

    # Сообщение о запуске бота
    dp.register_message_handler(send_to_admin_launch)
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    # Обработчик для отмены
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    # Обработчики для данных
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.descripption)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    # обработчик для проверка юзера на админа
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)