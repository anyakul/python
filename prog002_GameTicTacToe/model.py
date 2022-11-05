# 39) Создайте программу для игры в "Крестики-нолики".

from telegram import Update
from telegram.ext import CallbackContext
import datetime
from model import *
from spy_log import *
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

nums = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}


def build_menu(buttons, n_cols):
    return [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]


def get_buttons_list(new_nums):
    lst = list(new_nums.values())
    buttons = []

    for i in lst:
        buttons.append(InlineKeyboardButton(str(i), callback_data=str(i)))

    return InlineKeyboardMarkup(build_menu(buttons, n_cols=3))


def show_field(nums, message):
    bot.send_message(message.from_user.id, text=' '.join(
        '{}'.format(val) for key, val in nums.items()))


def reset_nums(nums):
    for key, val in nums.items():
        if key != '\nn':
            nums[key] = key


def check_win(nums):
    if (nums[1] == nums[2] == nums[3]) or \
        (nums[4] == nums[5] == nums[6]) or \
        (nums[7] == nums[8] == nums[9]) or \
        (nums[1] == nums[4] == nums[7]) or \
        (nums[2] == nums[5] == nums[8]) or \
        (nums[3] == nums[6] == nums[9]) or \
        (nums[1] == nums[5] == nums[9]) or \
            (nums[3] == nums[5] == nums[7]):
        return True
    else:
        return False


def check_draw(nums):
    count = -1
    for i in nums:
        if nums[i] == X or nums[i] == 0:
            count += 1
    if count == 9 and check_win(nums) == False:
        return True
    else:
        return False


def check_input(nums, num):
    if nums[num] == X or nums[num] == O:
        return False
    else:
        return True


def computer_move(nums):
    num = randint(1, 9)
    check_input(nums, num)

    while check_input(nums, num) == False:
        num = randint(1, 9)
        check_input(nums, num)
    
    return num


def player_move(move):
    return int(input(f'Введите незанятое число от 1 до 9 за {move}: '))


def get_num(id_player, computers_move):
    if id_player == computers_move:
        num = computer_move()
    else:
        num = computer_move()

    return num
