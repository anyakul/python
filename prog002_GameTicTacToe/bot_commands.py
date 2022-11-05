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


def play_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Игра крестики нолики')
    update.message.reply_text(f'Начало игры')
    computers_move = O
    id_player = X

    while check_win(nums) != True or check_draw(nums) != True:
        id_player = X if id_player == O else O
        if id_player == computers_move:
            num = computer_move(nums)
        elif id_player != computers_move:
            num = computer_move(nums)
            reply_markups = get_buttons_list(nums)
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Выберите число: ", reply_markup=reply_markups)
            updater.dispatcher.add_handler(CallbackQueryHandler(button))
        nums[num] = id_player
        check_draw(nums)
        check_win(nums)

    if check_draw(nums) == True:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=f'Ничья. Наберите /play чтобы играть снова')
    elif check_win(nums) == True:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f'Выиграл {id_player}. Наберите /play чтобы играть снова')


def button(update, _):
    query = update.callback_query
    input_num = query.data
    query.answer()
    print(input_num)
    query.edit_message_text(text=f"Выбранный вариант: {input_num}")

    return input_num
