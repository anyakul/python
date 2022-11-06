from telegram import Update
from telegram.ext import ContextTypes
from model import *

LBL_X = 'x'
LBL_O = 'o'

data = open('confident/token.txt', 'r')
token = data.read()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reset_nums(nums)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Привет, пользователь. Наберите x и число чтобы сделать ход'
    )


async def usr_msg_hdr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    msg.split(' ')
    ms = msg[0]
    num = int(msg[2])

    if ms.lower() == LBL_X:
        nums[num] = 'x'
        field = show_field(nums)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=field)
        if check_win(nums) == True:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='Выиграл X. Наберите /start чтобы играть снова')
        if check_draw(nums) == True:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='Ничья. Набирите /start чтобы играть снова')
    elif ms.lower() == LBL_O:
        nums[num] = 'o'
        await context.bot.send_message(chat_id=update.effective_chat.id, text=show_field(nums))
        if check_win(nums) == True:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='Выиграл O Набирите /start чтобы играть снова')
        if check_draw(nums) == True:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='Ничья. Набирите /start чтобы играть снова')
