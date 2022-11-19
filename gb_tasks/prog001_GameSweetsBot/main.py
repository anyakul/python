from model import *
import telebot


with open('confident/token.txt') as f:
    text = f.read()
bot = telebot.TeleBot(text)

start_text = f'''Игра с конфeтами. Правила игры:
Вы можете брать от {MIN_CANDY_STEP} до {MAX_CANDY_STEP} конфет за ход. Всего {CNT_CANDY} конфет. Выигрывает тот кто возьмет последние конфеты.
Игра началась'''


with open('confident/token.txt') as f:
    text = f.read()
bot = telebot.TeleBot(text)


computer_move = get_first_move()
max_step = CNT_CANDY
sum = 0


@bot.message_handler(commands=['start'])
def main(message):
    global player_move
    global sum
    sum = 0

    bot.send_message(message.chat.id, start_text)
    if computer_move == 1:
        sum = computers_move(MAX_CANDY_STEP)
        bot.send_message(
            message.chat.id, f'Бот ходит первым. Он взял {sum} конфет')
    msg = bot.send_message(
        message.chat.id, f"Введите число от {MIN_CANDY_STEP} до {MAX_CANDY_STEP}: ")
    bot.register_next_step_handler(msg, move)


@bot.message_handler(content_types=['text'])
def move(message):
    global sum
    global max_step

    if check_input(int(message.text), max_step):
        sum += int(message.text)
        bot.send_message(message.chat.id, f'Взято конфет: {sum}')
        max_step = get_max_step(sum)
        if sum < CNT_CANDY:
            sum += computers_move(max_step)
            max_step = get_max_step(sum)
            bot.send_message(
                message.chat.id, f'Взято конфет: {sum}. Вы можете взять от {MIN_CANDY_STEP} до {max_step} конфет:')
            if sum == CNT_CANDY:
                bot.send_message(
                    message.chat.id, f'Взято конфет: {sum}. Выиграл компьютер')
        else:
            bot.send_message(
                message.chat.id, f'Взято конфет: {sum}. Выиграл игрок. Нажмите /start чтобы начать заново')
    elif sum == CNT_CANDY:
        bot.send_message(
            message.chat.id, f'Взяты все конфеты. Нажмите /start чтобы начать снова')
    else:
        bot.send_message(
            message.chat.id, f'Вы можете взять от {MIN_CANDY_STEP} до {max_step} конфет:')


bot.polling(none_stop=True)
