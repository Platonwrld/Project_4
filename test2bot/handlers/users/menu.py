from loader import dp
from aiogram.dispatcher.filters import Command
from aiogram import types
from keyboards.default import kb_menu


@dp.message_handler(Command('menu'))
async def menu(message : types.Message):
    await message.answer('Choice number from menu below', reply_markup=kb_menu)