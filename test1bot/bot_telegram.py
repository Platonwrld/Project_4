from aiogram.utils import executor      # для того чтобы бот вышел в онлайн
import logging
from create_bot import dp
from handlers import client, admin, general
from database import sqlite_db


logging.basicConfig(level=logging.INFO)


# function for bot when he come up in online
# specifying service information
async def on_startup(_):
    print('Bot in online')
    sqlite_db.sql_start()


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
general.register_handlers_general(dp)


# if bot not online he won't get messages after he come up online, skip_updates do this
# skip old incoming updates from queue
# start long_polling it's like launch code that can get actions by users
# function on_startup written at the beginnning of he code 
# на самом деле start_polling делает метод get_updates на сервер телеграма
executor.start_polling(dp, skip_updates=True, on_startup=admin.send_to_admin_launch)