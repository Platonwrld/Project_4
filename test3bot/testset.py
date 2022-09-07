import logging
from main import dp
from aiogram.utils import executor
from handlers import client


logging.basicConfig(level=logging.INFO)

async def start_function():
    print('Bot in online!')


client.register_handlers_client(dp)


executor.start_polling(dp, skip_updates=True)