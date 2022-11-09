from spy_log import *
from model import *
import telebot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

with open('confident/token.txt') as f:
    text = f.read()
bot = telebot.TeleBot(text)

@bot.message_handler(commands=['start'])
def start_command(message):
    reply_markups = InlineKeyboardMarkup(build_menu(buttons_list, n_cols=3))
    bot.send_message(message.chat.id, text="Выберите число: ", reply_markup=reply_markups)
