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
        bot.send_message(message.from_user.id, 'Вітаємо вас у чат-боті онлайн платформи iMarket Магальської громади! 👋' +
                         ' Ми об’єднали всі магазини громади в одному місці, щоб зробити ваші покупки ще зручнішими та швидшими. '
                         'Тут ви можете дізнаватися про товари, акції, новинки та оформлювати покупки в будь-який час.'+ '\n' +
                         'Наш девіз: \n «iMarket — все поруч, все для вас!» Дякуємо, що обираєте нас! 🛍')
    elif message.text == 'Продуктові магазини':
        bot.send_message(message.from_user.id, "Тут список продуктових магазинів.", parse_mode='Markdown')
bot.polling(non_stop=True, interval=0)