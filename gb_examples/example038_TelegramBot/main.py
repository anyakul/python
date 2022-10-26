from telegram import Update
from telegram.ext import Updater, CommandHandler
from bot_commands import *

data = open('gb_examples/example038_TelegramBot/token.txt', 'r')
text = data.read()
updater = Updater(text)

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))

updater.start_polling()
updater.idle()
