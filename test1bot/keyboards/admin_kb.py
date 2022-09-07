from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


""" Buttons for admin keyboard """
load_but = KeyboardButton('/Загрузить')
del_but = KeyboardButton('/Удалить')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(load_but).add(del_but)