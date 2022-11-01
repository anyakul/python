from telegram import Update
from telegram.ext import Updater, CommandHandler
from bot_comands import *

data = open('confident/token.txt', 'r')
text = data.read()
updater = Updater(text)

updater.dispatcher.add_handler(CommandHandler('delt', delt_command))

updater.start_polling()
updater.idle()
