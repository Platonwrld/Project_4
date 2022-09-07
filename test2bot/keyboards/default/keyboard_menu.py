from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='10'),
            KeyboardButton(text='20')
        ],

        [
            KeyboardButton(text='100')
        ],

        [
            KeyboardButton(text='Subscribe'),
            KeyboardButton(text='Like'),
            KeyboardButton(text='Another')
        ]
    ],
    resize_keyboard=True
)