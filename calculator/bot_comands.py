from spy_log import *
from model import *
import telebot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

with open('confident/token.txt') as f:
    text = f.read()
bot = telebot.TeleBot(text)
'''
nums = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}


def build_menu(buttons, n_cols):
    return [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]


def get_buttons_list():
    lst = list(nums.values())
    buttons = []

    for i in lst:
        buttons.append(InlineKeyboardButton(str(i), callback_data=str(i)))

    return InlineKeyboardMarkup(build_menu(buttons, n_cols=3))
'''

@bot.message_handler(commands=['start'])
def start_command(message):
    reply_markups = InlineKeyboardMarkup(build_menu(buttons_list, n_cols=3))
    bot.send_message(message.chat.id, text="Выберите число: ", reply_markup=reply_markups)
