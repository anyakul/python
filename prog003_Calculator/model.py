import telebot

data = open('confident/token.txt', 'r')
token = data.read()
bot = telebot.TeleBot(token)


def draw_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    one_k = telebot.types.InlineKeyboardButton(text='1', callback_data='1')
    two_k = telebot.types.InlineKeyboardButton(text='2', callback_data='2')
    three_k = telebot.types.InlineKeyboardButton(text='3', callback_data='3')
    four_k = telebot.types.InlineKeyboardButton(text='4', callback_data='4')
    five_k = telebot.types.InlineKeyboardButton(text='5', callback_data='5')
    six_k = telebot.types.InlineKeyboardButton(text='6', callback_data='6')
    seven_k = telebot.types.InlineKeyboardButton(text='7', callback_data='7')
    eight_k = telebot.types.InlineKeyboardButton(text='8', callback_data='8')
    nine_k = telebot.types.InlineKeyboardButton(text='9', callback_data='9')
    plus_k = telebot.types.InlineKeyboardButton(text='+', callback_data='+')
    minus_k = telebot.types.InlineKeyboardButton(text='-', callback_data='-')
    mult_k = telebot.types.InlineKeyboardButton(text='*', callback_data='*')
    div_k = telebot.types.InlineKeyboardButton(text='/', callback_data='/')
    equil_k = telebot.types.InlineKeyboardButton(text='=', callback_data='=')
    reset_k = telebot.types.InlineKeyboardButton(text='C', callback_data='C')
    keyboard.add(one_k, two_k, three_k)
    keyboard.add(four_k, five_k, six_k)
    keyboard.add(seven_k, eight_k, nine_k)
    keyboard.add(plus_k, minus_k, mult_k)
    keyboard.add(div_k, equil_k, reset_k)

    return keyboard
