import os
import telebot
from dotenv import load_dotenv,find_dotenv

from commands import message_hendler, callback_query
load_dotenv(find_dotenv())
bot = telebot.TeleBot(token=os.getenv('TOKEN'))

message_hendler(bot)
callback_query(bot)


bot.polling(non_stop=True)

