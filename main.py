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
        bot.send_message(message.from_user.id, '👋 Привіт у iMagala Delivery! 🚀' +
                         '\nХочеш швидку доставку?\nМи вже в дорозі! '
                         'Обирай товари — ми доставимо їх просто до тебе додому.'+ '\n' +
                         'iDelivery — замовив і вже чекаєш! 😎', reply_markup=markup)
    elif message.text == 'Продукти харчування':
        bot.send_message(message.from_user.id, 'Тут список продуктових товарів.', parse_mode="Markdown")
    elif message.text == 'Про нас':
        bot.send_message(message.from_user.id, "Розроблено для громади.\nРозробники:\nЯкобець Д.Г,\nЯкобець Г.С,\nГостюк К.І", parse_mode='Markdown')

bot.polling(non_stop=True, interval=0)