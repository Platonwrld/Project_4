from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


""" Buttons for main menu """

kb_menu = ReplyKeyboardMarkup(

    keyboard=[

    [
        KeyboardButton(text='Что такое Ton?'),
        KeyboardButton(text='Как работает TVM?')
    ],

    [
        KeyboardButton(text='Основные инструменты для разработчиков TON'),
    ],

    [
        KeyboardButton(text='Отличие TON и Everscale'),
    ]

    ],
    resize_keyboard=True

)





