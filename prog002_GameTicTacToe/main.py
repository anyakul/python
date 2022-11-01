from telegram import Update
from telegram.ext import Updater, CommandHandler
from bot_commands import *

data = open('confident/token.txt', 'r')
text = data.read()
updater = Updater(text)


CNT_CANDY = 100
CNT_PLAYERS = 2
MIN_CANDY_STEP = 1
MAX_CANDY_STEP = 28

num = 0
updater.dispatcher.add_handler(CommandHandler('play', play_command))
updater.start_polling()
updater.idle()
