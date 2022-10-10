# 38) Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


from random import randint


START_NUM = '2021'
MODE_1 = 'computer'
MODE_2 = 'person'


def check_input(num):
    if num < 1 or num > 28:
        return False
    else:
        return True


def computers_move():
    return randint(1, 28)


def player_move():
    num = int(input(f'Введите число от 1 до 28: '))
    check_input(num)
    while check_input(num) == False:
        num = int(input(f'Введите число от 1 до 28: '))
        check_input(num)

    return num


def get_win(count_move):
    if count_move % 2 == 0:
        print('Выиграл второй игрок')
    else:
        print('Выиграл первый игрок')


def play_game(mode, computer_move='no'):
    num = 100
    count_move = 0

    while num > 0:
        if mode == 'person':
            input_num = player_move()
        elif mode == 'computer':
            if count_move % 2 == computer_move:
                input_num = computers_move()
            else:
                input_num = player_move()

        num -= input_num
        print(f'Осталось конфет {num}')
        count_move += 1

    get_win(count_move)


mode_num = int(input('Выберите режим (1 - с компьютером, 2 - с человеком): '))

if mode_num == 1:
    mode = MODE_1
if mode_num == 2:
    mode = MODE_2


move = randint(0, 1)
play_game(mode, move)
