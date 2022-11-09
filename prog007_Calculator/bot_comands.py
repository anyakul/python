from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Updater, CallbackQueryHandler
import datetime
from model import *

data = open('confident/token.txt', 'r')
token = data.read()
updater = Updater(token)
bot = telebot.TeleBot(token)


def start_command(update: Update, context: CallbackContext):
    reply_markups = get_buttons_list()
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Калькулятор", reply_markup=reply_markups)

