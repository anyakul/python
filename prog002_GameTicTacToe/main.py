from model import *
import telebot

player_move = get_first_move()
computer_move = get_computer_move(player_move)


with open('confident/token.txt') as f:
    text = f.read()
bot = telebot.TeleBot(text)


@bot.message_handler(commands=['start'])
def main(message):
    global player_move
    reset_nums(nums)
    msg = bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>\nИгра крестики нолики началась!".format(
        message.from_user, bot.get_me()), parse_mode='html')
    bot.send_message(message.chat.id, show_field(nums))
    if computer_move == X:
        nums[computers_move(nums)] = computer_move
        bot.send_message(message.chat.id, show_field(nums))
    msg = bot.send_message(
        message.chat.id, f"Введите незанятое число за {player_move}: ")
    bot.register_next_step_handler(msg, move)


@bot.message_handler(content_types=['text'])
def move(message):
    global nums

    if check_input(nums, int(message.text)):
        nums[int(message.text)] = player_move
        bot.send_message(message.chat.id, show_field(nums))
        if check_win(nums) or check_draw(nums):
            res_str = get_res_str(nums, player_move)
            bot.send_message(message.chat.id, text=res_str)
        else:
            num = computers_move(nums)
            nums[num] = computer_move
            bot.send_message(message.chat.id, show_field(nums))
            if check_win(nums) or check_draw(nums):
                res_str = get_res_str(nums, computer_move)
                bot.send_message(message.chat.id, text=res_str)
    else:
        bot.send_message(
            message.chat.id, f'Это число занято. Выберите другое:')


bot.polling(none_stop=True)
