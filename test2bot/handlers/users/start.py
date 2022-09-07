from aiogram import types
from loader import dp


@dp.message_handler(text='/start')
async def command_start(message : types.Message):

    await message.answer(f"Hello {message.from_user.full_name}! \n"
                         f"Your id {message.from_user.id}")