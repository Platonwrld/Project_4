from aiogram import Dispatcher, types
from create_bot import dp, bot
import json, string

""" General part """
# декоратор обозначающий, что когда что то будет попадать в чат, то ...
# деоратор улавливает любые сообщения, обработчик сообщений 
# @dp.message_handler()
async def echo_send(message : types.Message):
    if message.text == 'Привет':
        await message.answer('Hello!')
    
    if message.text == 'Как дела?':
        await message.answer('All good')

    # 1. for i in message.text.split(' ') - каждое словво в сообщении это i
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('mat.json')))) != set():
        await message.reply('Материться запрещено!')
        await message.delete()
     
    # await message.reply(message.text)   # будет сообщение якобы переслать + ехо
    # message.from_user.id - getting id by user
    # await message.bot.send_message(message.from_user.id, message.text)


# @dp.message_handler()
# async def delete_mat(message : types.Message):
    # 1. for i in message.text.split(' ') - каждое словво в сообщении это i
    # if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
    #     .intersection(set(json.load(open('mat.json')))) != set():
    #     await message.reply('Материться запрещено')
    #     await message.delete()

def register_handlers_general(dp : Dispatcher):

    dp.register_message_handler(echo_send)