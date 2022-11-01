from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy_log import *
from model import *


CNT_CANDY = 100
CNT_PLAYERS = 2
MIN_CANDY_STEP = 1
MAX_CANDY_STEP = 28


def play_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Игра с конфатами')
    update.message.reply_text(f'Начало игры')
    update.message.reply_text(f'Вы можете взять от {MIN_CANDY_STEP} до {MAX_CANDY_STEP} конфет')
    play_func()


def move_command(update: Update, context: CallbackContext):
    log(update, context)
    play_func()


def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')
