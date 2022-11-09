from model import *


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = draw_keyboard()
    bot.send_message(message.chat.id, 'Калькулятор', reply_markup=keyboard)
