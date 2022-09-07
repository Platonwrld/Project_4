from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# каждые кнопки по отдельности
but1 = KeyboardButton('/Инструменты')
but2 = KeyboardButton('/Сервисы')
but3 = KeyboardButton('/Меню')

but4 = KeyboardButton('Поделиться номером', request_contact=True)
but5 = KeyboardButton('Поделиться локацией', request_location=True)

# замещение обычной клавиатуры и добавление необходимых кнопок
# insert - добавление кнопки на последнюю строку
# resize_keyboard=True - маленький размер
# one_time_keyboard=True появляется один раз и исчезает
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

# add(but1). row, insert - last row
kb_client.add(but3).row(but1, but2).row(but4, but5)

""" Buttons for main menu """
mbut1 = KeyboardButton('/Что такое Ton?')
mbut2 = KeyboardButton('/Как работает TVM?')
mbut3 = KeyboardButton('/Основные инструменты для разработчиков TON')
mbut4 =  KeyboardButton('/Отличие TON и Everscale'),

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.row(mbut1, mbut2).add(mbut3).add(mbut4)
