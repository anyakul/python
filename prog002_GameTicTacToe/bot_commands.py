from telegram import Update
from telegram.ext import CallbackContext
import datetime
from model import *
from spy_log import *

def play_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Игра крестики нолики')
    update.message.reply_text(f'Начало игры')
    play_func()
    update.message.reply_text(' '.join('{}'.format(val) for key, val in nums.items()))
"""
def play_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Игра крестики нолики')
    update.message.reply_text(f'Начало игры')
    id_player = X
    count_move = 0
    check_win(nums)

    while check_win(nums) == False or check_draw(nums, count_move) == False:
        num = get_num(id_player, computer_move)

        if check_input(nums, num) == True:
            count_move += 1
            if do_move(nums, num, id_player, count_move) != 'no':
                id_player = do_move(nums, num, id_player, count_move)
                show_field(update: Update, context: CallbackContext)
            else:
                show_field(update, context)
                break
        else:
            num = get_num(id_player, computer_move)
            continue
"""
