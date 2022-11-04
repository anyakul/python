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


def computer_move(max_step):
    return randint(MIN_CANDY_STEP, max_step)


def check_input(num, max_step):
    if num >= MIN_CANDY_STEP and num <= max_step:
        return True
    else:
        return False


def get_max_step(num):
    res = MAX_CANDY_STEP

    if num >= CNT_CANDY - MAX_CANDY_STEP:
        res = CNT_CANDY - num

    return res


@bot.message_handler(content_types=['text'])
def play_func(message):
    input_num = 0
    num = 0
    id_player = 2
    id_computer_player = 2

    while num < CNT_CANDY:
        max_step = get_max_step(num)
        if id_player == id_computer_player:
            input_num = computer_move(max_step)
            id_player = 1 if id_player == 2 else 2
            print(f"комп - {input_num}")
        elif id_player != id_computer_player:
            bot.send_message(
                message.from_user.id, text=f'Вы можете взять от {MIN_CANDY_STEP} до {max_step} конфет: ')
            if message.text == '/play':
                return
            msg = bot.send_message(message.from_user.id,
                                   text=f"{message.text}")
            bot.register_next_step_handler(msg, play_func)
            input_num = int(msg.text)
            print(f"мы - {input_num}")
            id_player = 1 if id_player == 2 else 2
        num += input_num
        bot.send_message(message.from_user.id, text=f'Взято конфет: {num}')

    bot.send_message(message.from_user.id,
                     text=f"Победу одержал {PLAYERS_NAMES[1 if id_player == 2 else 2]}")


bot.polling(none_stop=True, interval=0)
