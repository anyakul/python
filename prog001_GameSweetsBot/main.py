from model import *
import time
import telebot


with open('confident/token.txt') as f:
    text = f.read()
bot = telebot.TeleBot(text)

start_text = f'''Игра с конфeтами. Правила игры:
Вы можете брать от {MIN_CANDY_STEP} до {MAX_CANDY_STEP} конфет за ход. Всего {CNT_CANDY} конфет. Выигрывает тот кто возьмет последние конфеты.
Игра началась'''


@bot.message_handler(commands=['start'])
def main(message):
    global sum
    msg = bot.send_message(message.chat.id, start_text)
    bot.send_message(
        message.chat.id, f"Вы можете взять от {MIN_CANDY_STEP} до {MAX_CANDY_STEP} конфет: ")
    move_time = 10
    computer_move = 2
    id_player = 2

    while sum <= CNT_CANDY:
        max_step = get_max_step(sum)
        if id_player == computers_move:
            sum += computers_move(max_step)
        elif id_player != computer_move:
            msg = bot.send_message(
                message.chat.id, f"Вы можете взять от {MIN_CANDY_STEP} до {max_step} конфет: ")
            bot.register_next_step_handler(msg, move)
            time.sleep(move_time)
        bot.send_message(message.chat.id, f'Взято {sum} конфет')
        if sum <= CNT_CANDY:
            id_player = 1 if id_player == 2 else 2
    bot.send_message(chat_id=message.chat.id,
                     text=f"Победу одержал {PLAYERS_NAMES[1 if id_player == 2 else 2]}")


@bot.message_handler(content_types=['text'])
def move(message):
    global sum
    sum += int(message.text)


bot.polling(none_stop=True)
