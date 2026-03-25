import telebot
from telebot import types
from apisetup import api
t_token = api
bot = telebot.TeleBot(t_token)

@bot.message_handler(commands=['/start'])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Продукти')


bot.polling(non_stop=True, interval=0)