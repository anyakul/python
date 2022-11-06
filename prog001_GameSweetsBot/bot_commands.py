from telegram import Update
from telegram.ext import Updater, CallbackQueryHandler
from model import *
from spy_log import *
import telebot

data = open('confident/token.txt', 'r')
token = data.read()
updater = Updater(token)
bot = telebot.TeleBot(token)

start_text = f'''Игра с конфeтами. Правила игры:
Вы можете брать от {MIN_CANDY_STEP} до {MAX_CANDY_STEP} конфет за ход. Всего {CNT_CANDY} конфет. Выигрывает тот кто возьмет последние конфеты.
Наберите /play чтобы начать.'''

play_text = f'''Игра с конфетами началась.
Вы можете взять от {MIN_CANDY_STEP} до {MAX_CANDY_STEP} конфет'''


def start_command(update: Update, context: CallbackContext):
    log(update, context)
    context.bot.send_message(chat_id=update.effective_chat.id, text=start_text)


@bot.message_handler(content_types=['text'])
def play_command(update: Update, context: CallbackContext):
    log(update, context)
    context.bot.send_message(chat_id=update.effective_chat.id, text=play_text)
    input_num = 0
    num = 0
    id_player = 2
    id_computer_player = 2
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    while num < CNT_CANDY:
        max_step = get_max_step(num)
        if id_player == id_computer_player:
            input_num = computer_move(max_step)
        elif id_player != id_computer_player:
            reply_markups = get_buttons_list(MIN_CANDY_STEP, max_step)
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Выберите число: ", reply_markup=reply_markups)
        num += input_num
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=f'Взято конфет: {num}')
        id_player = 1 if id_player == 2 else 2

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Победу одержал {PLAYERS_NAMES[1 if id_player == 2 else 2]}")
    updater.dispatcher.remove_handler(CallbackQueryHandler(button))


def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Неизвестная команда. Отправьте /play для начала игры')


def button(update, _):
    query = update.callback_query
    input_num = query.data
    query.answer()
    print(input_num)
    query.edit_message_text(text=f"Выбранный вариант: {input_num}")

    return input_num
