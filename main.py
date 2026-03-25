import telebot
from telebot import types
from apisetup import api
t_token = api
bot = telebot.TeleBot(t_token)

@bot.message_handler(commands=['/start'])
def send_message(message):
    markup = types.ReplyKeyboardMarkup()


bot.polling(non_stop=True, interval=0)