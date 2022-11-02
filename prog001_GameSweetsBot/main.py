from telegram import Update
from telegram.ext import Updater, CommandHandler
from bot_commands import *

data = open('confident/token.txt', 'r')
text = data.read()
updater = Updater(text)

updater.dispatcher.add_handler(CommandHandler('start', start_command))
updater.dispatcher.add_handler(CommandHandler('play', play_command))
updater.start_polling()
updater.idle()