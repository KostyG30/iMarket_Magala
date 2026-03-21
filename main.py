import telebot
from telebot import types
from  apisetup import api
t_token = api
bot = telebot.TeleBot(t_token)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #create buttons
        btn1 = types.KeyboardButton('Продукти харчування')
        btn2 = types.KeyboardButton('Одяг')
        btn3 = types.KeyboardButton('Іграшки')
        btn4 = types.KeyboardButton('Про нас')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, 'Вітаємо вас у мережі магазинів iMarket Магальської громади!' +
                         ' Ми раді бачити вас серед наших клієнтів і щодня працюємо для вашого комфорту, якості та вигідних покупок.'+ '\n' +
                         'Наш девіз: \n «iMarket — поруч, вигідно, з турботою про кожного!»' +
                         ' Завітавши до нас, ви обираєте надійність, доступність і сучасний сервіс. '
                         'Дякуємо, що ви з нами!')
    elif message.text == 'Продуктові магазини':
        bot.send_message(message.from_user.id, "Тут список продуктових магазинів.", parse_mode='Markdown')
bot.polling(non_stop=True, interval=0)