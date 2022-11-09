from model import *
from spy_log import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton


def build_menu(buttons, n_cols):
    return [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]


buttons_list = [
    InlineKeyboardButton("1", callback_data="1"),
    InlineKeyboardButton("2", callback_data="2"),
    InlineKeyboardButton("3", callback_data="3"),
    InlineKeyboardButton("4", callback_data="4"),
    InlineKeyboardButton("5", callback_data="5"),
    InlineKeyboardButton("6", callback_data="6"),
    InlineKeyboardButton("7", callback_data="7"),
    InlineKeyboardButton("8", callback_data="8"),
    InlineKeyboardButton("9", callback_data="9"),
    InlineKeyboardButton("+", callback_data="+"),
    InlineKeyboardButton("-", callback_data="-"),
    InlineKeyboardButton("*", callback_data="*"),
    InlineKeyboardButton("/", callback_data="/"),
    InlineKeyboardButton("=", callback_data="="),
    InlineKeyboardButton("C", callback_data="C")
]


def get_keyboard():
    print(buttons_list)
    return InlineKeyboardMarkup(build_menu(buttons_list, n_cols=3))
