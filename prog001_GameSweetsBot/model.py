from email import message
from random import randint
from telegram import Update
from telegram.ext import CallbackContext
#from telebot import Bot
import telebot

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


def sum(num, start_sum):
    start_sum + num


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


def calc():
    num = message.text.split()
    number = int(num)
    bot.send_message(message.chat.id, f'{number}')


def sum(num):
    return num


@bot.message_handler(content_types=['text'])
def play_func(message):
    input_num = 0
    num = 0
    id_player = 2
    id_computer_player = 2

    while num < CNT_CANDY:
        if id_player == id_computer_player:
            input_num = computer_move()
            id_player = 1 if id_player == 2 else 2
            print(f"комп - {input_num}")
        elif id_player != id_computer_player:
            if message.text == '/play':
                return
            msg = bot.send_message(message.from_user.id, text=f"{message.text}")
            bot.register_next_step_handler(msg, play_func)
            input_num = int(msg.text)
            print(f"мы - {input_num}")
            id_player = 1 if id_player == 2 else 2
        num += input_num
        bot.send_message(message.from_user.id, text=f'Взято конфет: {num}')

    bot.send_message(message.from_user.id, text=f"Победу одержал {PLAYERS_NAMES[1 if id_player == 2 else 2]}")


bot.polling(none_stop=True, interval=0)
