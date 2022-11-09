from telegram.ext import Updater, CommandHandler
from bot_comands import *

with open('confident/token.txt') as f:
    text = f.read()
updater = Updater(text)

updater.dispatcher.add_handler(CommandHandler('delt', delt_command))

updater.start_polling()
updater.idle()
