from telegram import Update
from telegram.ext import CallbackContext
import datetime
from spy_log import *


def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')


def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hi\n/time\n/help\n/sum')


def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')


def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text  # ~input
    print(msg)
    items = msg.split()  # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')  # ~print


def delt_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text  # ~input
    index = msg.find(' ')
    msg = msg[index + 1:]

    update.message.reply_text(
        f'{" ".join([i for i in msg.split() if not "абв" in i])}')
