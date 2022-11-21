from model import *
import telebot

result = 0
current_lst = []

data = open('confident/token.txt', 'r')
token = data.read()
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.chat.id, rules)
    bot.register_next_step_handler(msg, move)


@bot.message_handler(content_types=['text'])
def move(message):
    global result
    if len(current_lst) == 0 or current_lst[len(current_lst) - 1] in signs:
        if message.text.isdigit():
            current_num = int(message.text)
            sign = get_sign(current_lst)
            if sign == '/' and current_num == 0:
                bot.send_message(
                    message.chat.id, f'На 0 делить нельзя. Введите другое число')
            else:
                current_lst.append(str(current_num))
                result = get_result(result, sign, current_num)
                bot.send_message(
                    message.chat.id, f'Результат: {result}:')
        else:
            bot.send_message(
                message.chat.id, f'Введите число')
    if len(current_lst) == 0 or current_lst[len(current_lst) - 1].isdigit():
        if message.text in signs:
            sign = message.text
            current_lst.append(sign)
            bot.send_message(message.chat.id, f'Число: ')
        elif message.text == '=':
            bot.send_message(
                message.chat.id, f'{" ".join(current_lst)} = {str(result)}')
            bot.send_message(
                message.chat.id, 'Наберите /start чтобы начать заново. Или знак чтобы продолжить')
        else:
            bot.send_message(
                message.chat.id, f'Знак:')


bot.polling(none_stop=True)
