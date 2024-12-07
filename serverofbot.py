import telebot;
from conf import api
bot = telebot.TeleBot(api)

bot.polling(none_stop=True, interval=0)