import telebot
from telebot import types
from  apisetup import api
t_token = api
bot = telebot.TeleBot(t_token)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #create buttons
        btn1 = types.KeyboardButton('Продуктові магазини')
        btn2 = types.KeyboardButton('Все для дому')
        btn3 = types.KeyboardButton('Іграшки')
        btn4 = types.KeyboardButton('Про нас')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, 'Ласкаво просимо до мережі магазинів iMarket', reply_markup=markup)

bot.polling(non_stop=True, interval=0)