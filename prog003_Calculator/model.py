# 39) Создайте программу для игры в "Крестики-нолики".

from telegram import Update
from telegram.ext import CallbackContext
import datetime
from model import *
from random import randint
import telebot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

X = 'X'
O = '0'
MODE_1 = 'computer'
MODE_2 = 'person'

data = open('confident/token.txt', 'r')
token = data.read()
bot = telebot.TeleBot(token)

lst = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", "=", "C"]


def build_menu(buttons, n_cols):
    return [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]


def get_buttons_list():
    buttons = []

    for i in lst:
        buttons.append(InlineKeyboardButton(str(i), callback_data=str(i)))

    return InlineKeyboardMarkup(build_menu(buttons, n_cols=3))
