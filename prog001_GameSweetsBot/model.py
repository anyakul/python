from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from random import randint

MODE_1 = 'computer'
MODE_2 = 'person'
CNT_CANDY = 100
CNT_PLAYERS = 2
MIN_CANDY_STEP = 1
MAX_CANDY_STEP = 28

PLAYERS_NAMES = {
    1: 'Player_1',
    2: 'Player_2'
}


def computer_move(max_step):
    return randint(MIN_CANDY_STEP, max_step)


def get_max_step(num):
    res = MAX_CANDY_STEP

    if num >= CNT_CANDY - MAX_CANDY_STEP:
        res = CNT_CANDY - num

    return res


def build_menu(buttons, n_cols):
    return [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]


def get_buttons_list(min_num, max_num):
    lst = []

    for i in range(min_num, max_num):
        lst.append(InlineKeyboardButton(str(i), callback_data=str(i)))

    return InlineKeyboardMarkup(build_menu(lst, n_cols=5))
