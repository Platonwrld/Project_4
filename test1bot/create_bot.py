import asyncio
from aiogram import Bot
from aiogram.dispatcher import Dispatcher        # позволяет улавливать сообщения и отвечать определнной реакцией 
import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage    # class MemoryStorage allow to storage data in RAM memory


storage = MemoryStorage()     # создание экземпляра 

# создание потока
loop = asyncio.get_event_loop()

""" Фактически здесь создается экземпляр бота """
# aiogram have 2 types buttons: кнопки клавиатуры и инлайн кнопки(нажав на которые, отправляются сообщения в чат или боту)


# BOT INITIALIZATION
bot = Bot(token=config.TOKEN, parse_mode='HTML')

# DISPATCHER INIT
# class tha will be process incoming users actions
# обработчик
dp = Dispatcher(bot, storage=storage)       # adding example of class MemoryStorage in dp


