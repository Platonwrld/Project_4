from aiogram import types
from loader import bot

async def set_default_commands(dp):

    await bot.set_my_commands([
        types.BotCommand('start', 'Start bot'),
        types.BotCommand('help', 'Get help'),
    ])