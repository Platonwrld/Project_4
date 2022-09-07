from aiogram import Bot, types, Dispatcher
from data import config


""" OWN BOT EXAMPLE WITH TOKEN """
bot = Bot(token=config.BOT_TOKEN, parse_mode = types.ParseMode.HTML)
dp = Dispatcher(bot)