from dis import dis
from create_bot import dp, bot
from aiogram import Dispatcher, types
from keyboards import kb_client, kb_menu
from database import sqlite_db
from aiogram.dispatcher.filters import Command


""" Client part """
# commands - на какие команды будет реагировать этот обработчик
# @dp.message_handler(commands=['start', 'help'])     # сработает на /start and /help
# reply_markup параметр в который передается клавиатура 


async def commands_start(message : types.Message):

    try:
        await bot.send_message(message.from_user.id, 'Ты уже в TON!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Напишиет напрямую боту: \nhttp://t.me/myfirsttestbotforton_bot')


async def get_menu(message: types.Message):

    await message.answer('What question you interested?', reply_markup=kb_menu)


# @dp.message_handler(commands=['instruments'])
async def get_instruments(message : types.Message):

    await bot.send_message(message.from_user.id, 'TonDev, Tonos-cli, Ton.live.org')


# @dp.message_handler(commands=['services'])
async def get_actions(message : types.Message):

    await bot.send_message(message.from_user.id, 'Create smart-contract, deploy smart-contract, create applicateion based on TON')

# Обработчик команд, которые не существуют
# async def empty(message: types.Message):

#     await message.answer('Нет такой команды')
#     await message.delete()


async def word(message: types.Message):

    await message.answer('Сам дурак')


# Выгрузка данных из бд по запросу с кнопки
async def menu_command(message: types.Message):
    await sqlite_db.sql_read(message)



# function with handlers that will be send in main file where start bot
def register_handlers_client(dp : Dispatcher):

    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(get_menu, Command('menu'))
    dp.register_message_handler(get_instruments, commands=['Инструменты'])
    dp.register_message_handler(get_actions, commands=['Сервисы'])
    # dp.register_message_handler(empty)
    dp.register_message_handler(word, lambda message: 'дурак' in message.text)
    dp.register_message_handler(menu_command, commands=['Меню'])


