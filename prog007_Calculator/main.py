from telegram import Update
from telegram.ext import Updater, CommandHandler
from bot_comands import *
from telegram.ext import CommandHandler, MessageHandler, Filters
import telebot


with open('confident/token.txt') as f:
    text = f.read()
bot = telebot.TeleBot(text)

dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start_command)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()
