from email import message
from random import randint
from telegram import Update
from telegram.ext import CallbackContext
#from telebot import Bot
import telebot
import time

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

data = open('confident/token.txt', 'r')
token = data.read()
bot = telebot.TeleBot(token)

storage = {}



def echo(message):
    num = bot.send_message(message.chat.id, text=f"{message.text}")
    print(type(num.text))


def init_storage(user_id):
    storage[user_id] = dict(first_number=None)


def store_number(user_id, key, value):
    storage[user_id][key] = dict(value=value)


def get_number(user_id, key):
    return storage[user_id][key].get('value')


def computer_move():
    return randint(MIN_CANDY_STEP, MAX_CANDY_STEP)


def check_input(num):
    if num >= MIN_CANDY_STEP and num <= MAX_CANDY_STEP:
        return True
    else:
        return False


def player_move():
    num = int(
        input(f'Вы можете взять от {MIN_CANDY_STEP} до {MAX_CANDY_STEP} конфет: '))
    check_input(num)
    while check_input(num) == False:
        num = int(
            input(f'Вы можете взять от {MIN_CANDY_STEP} до {MAX_CANDY_STEP} конфет: '))
        check_input(num)

    return num





#bot.skip_pending = True
bot.polling(none_stop=True)


def start_2(message):
    return message.text

