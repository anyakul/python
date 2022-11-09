from model import *
import time
import telebot

player_move = get_first_move()


with open('confident/token.txt') as f:
    text = f.read()
bot = telebot.TeleBot(text)


@bot.message_handler(commands=['start'])
def main(message):
    global player_move
    reset_nums(nums)
    msg = bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>\nИгра крестики нолики началась!".format(
        message.from_user, bot.get_me()), parse_mode='html')
    id_player = X
    computer_move = get_computer_move(player_move)
    count_move = 0
    move_time = 10

    while not check_win(nums) and not check_draw(nums, count_move):
        if id_player == computer_move:
            nums[computers_move(nums)] = computer_move
        elif id_player != computer_move:
            msg = bot.send_message(
                message.chat.id, f"Введите незанятое число. Ход переключится через {move_time} секунд: ")
            bot.register_next_step_handler(msg, move)
            time.sleep(move_time)
        count_move += 1
        if not check_win(nums) and not check_draw(nums, count_move):
            bot.send_message(message.chat.id, show_field(nums))
            id_player = X if id_player == O else O
    if check_win(nums) or check_draw(nums, count_move):
        bot.send_message(message.chat.id, show_field(nums))
        res_str = get_res_str(id_player, nums, count_move)
        bot.send_message(message.chat.id, text=res_str)


@bot.message_handler(content_types=['text'])
def move(message):
    global nums
    global player_move
    nums[int(message.text)] = player_move


bot.polling(none_stop=True)
