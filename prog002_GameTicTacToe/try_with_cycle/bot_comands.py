from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Updater, CallbackQueryHandler
import datetime
from model import *
from spy_log import *

data = open('confident/token.txt', 'r')
token = data.read()
updater = Updater(token)
bot = telebot.TeleBot(token)

start_text = f'''Игра с В крестики-нолики 3х3.
Наберите /play чтобы начать.'''

play_text = f'''Игра в крестики-нолики началась.'''


def start_command(update: Update, context: CallbackContext):
    log(update, context)
    context.bot.send_message(chat_id=update.effective_chat.id, text=start_text)


def play_command(update: Update, context: CallbackContext):
    reset_nums(nums)
    log(update, context)
    update.message.reply_text(play_text)
    computers_move = O
    id_player = X
    check_draw(nums)
    check_win(nums)
    num = 0

    while check_win(nums) != True and check_draw(nums) != True:
        if id_player == computers_move:
            num = computer_move(nums)
        elif id_player != computers_move:
            num = computer_move(nums)
        nums[num] = id_player
        reply_markups = get_buttons_list(nums)
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Выберите число: ", reply_markup=reply_markups)
        updater.dispatcher.add_handler(CallbackQueryHandler(button))
        nums[num] = id_player
        if check_draw(nums) == False and check_win(nums) == False:
            id_player = X if id_player == O else O
    if check_draw(nums) == True:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f'Ничья. Наберите /play чтобы играть снова')
    if check_win(nums) == True:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f'Выиграл {id_player}. Наберите /play чтобы играть снова')


def button(update, _):
    query = update.callback_query
    input_num = query.data
    query.answer()
    print(input_num)
    query.edit_message_text(text=f"Выбранный вариант: {input_num}")

    return input_num


def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Неизвестная команда. Отправьте /play для начала игры')
