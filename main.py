from telegram import Update
from telegram.ext import Updater, CommandHandler
from bot_commands import *
from telegram.ext import CommandHandler, MessageHandler, Filters
from bot_commands import *

dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start_command)
dispatcher.add_handler(start_handler)
play_handler = CommandHandler('play', play_command)
dispatcher.add_handler(play_handler)
updater.dispatcher.add_handler(CallbackQueryHandler(button))

#echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
#dispatcher.add_handler(echo_handler)
#inline_caps_handler = InlineQueryHandler(inline_caps)
#updater.dispatcher.add_handler(inline_caps_handler)

updater.start_polling()
updater.idle()