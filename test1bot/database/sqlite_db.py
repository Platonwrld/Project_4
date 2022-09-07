from os import curdir
import sqlite3 as sq
from aiogram import types
from create_bot import *


""" Function that create db or connect to db that exists """
def sql_start():

    global base, cur

    base = sq.connect('test_db.db')
    cur = base.cursor()     # part from db that implement search, sorting and show result

    if base:
        print('DB connected!')
    
    # PRIMARY KEY mean that name won't be repeated
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


# function that will be fix changes in db
async def sql_add_command(state):

    async with state.proxy() as data:

        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):

    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[2]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')


async def sql_read2():

    return cur.execute('SELECT * FROM menu').fetchall()


""" Функция для удаления айтема """
async def sql_delete_command(data):

    cur.execute('DELETE FROM menu WHERE name == ?', (data,))
    base.commit()
