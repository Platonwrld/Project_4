from main import dp, bot
from aiogram import Dispatcher, types
from keyboards import kb_menu
from aiogram.dispatcher.filters import Command


async def get_menu(message: types.Message):

    await message.answer('What question you interested?', reply_markup=kb_menu)


# async def command_start(message : types.Message):

#     try:
#         await bot.send_message(message.from_user.id, f'Hello, {message.from_user.full_name}!\nTon helper ready to help you', reply_markup=kb_client)
#         await message.delete()
#     except:
#         await message.reply('Type there: \nhttp://t.me/ton_helper_for_dev_bot')


async def replies_1(message : types.Message): 
            await message.reply('Telegram Open Netowrk')

async def replies_2(message : types.Message): 
            await message.reply('Telegram Virtual Machine')

async def replies_3(message : types.Message): 
            await message.reply('Toncli, Tondev, Tonos-cli')

async def replies_4(message : types.Message): 
            await message.reply('Два разных блокчейна, но их связывает одно - Ton-Blockcahin')



async def get_instruments(message: types.Message):

    await bot.send_message(message.from_user.id, 'TonDev, TonCli, Lite-Client')


def register_handlers_client(dp : Dispatcher):

    dp.register_message_handler(get_menu, Command('menu'))
    # Replies on question from kb_menu
    dp.register_message_handler(replies_1, text='Что такое Ton?')
    dp.register_message_handler(replies_2, text='Как работает TVM?')
    dp.register_message_handler(replies_3, text='Основные инструменты для разработчиков TON')
    dp.register_message_handler(replies_4, text='Отличие TON и Everscale')

    # Handler for /start and /help
    # dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(get_instruments, commands=['tools'])