from telegram import Update
from telegram.ext import CallbackContext
import datetime
from model import *
from spy_log import *
import telebot

data = open('confident/token.txt', 'r')
token = data.read()
bot = telebot.TeleBot(token)

def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')


CNT_CANDY = 100
CNT_PLAYERS = 2
MIN_CANDY_STEP = 1
MAX_CANDY_STEP = 28


def start_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Игра с конфeтами. Правила игры:\nВы можете брать от {MIN_CANDY_STEP} до {MAX_CANDY_STEP} конфет за ход. Всего {CNT_CANDY} конфет. Выингрывает тот кто возьмет последние конфеты.\nНаберите /play чтобы начать.')


def get_num(update: Update, context: CallbackContext):
    return update.message.text


def play_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Игра с конфатами')
    update.message.reply_text(f'Начало игры')
    update.message.reply_text(f'Вы можете взять от {MIN_CANDY_STEP} до {MAX_CANDY_STEP} конфет')
    play_func(message)
