from telegram import Update
from telegram.ext import CallbackContext
from spy_log import *


PATTERN = 'абв'  # ~print


def delt_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    index = msg.find(' ')
    msg = msg[index + 1:]

    update.message.reply_text(
        f'{" ".join([i for i in msg.split() if not PATTERN in i])}')
