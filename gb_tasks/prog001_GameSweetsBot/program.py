# 38) Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


from random import randint

MODE_1 = 'computer'
MODE_2 = 'person'
CNT_CANDY = 100
CNT_PLAYERS = 2
MIN_CANDY_STEP = 1
MAX_CANDY_STEP = 28

PLAYERS_NAMES = {
    1: 'Player_1',
    2: 'Player_2'
}


def check_input(num, max_step):
    if num >= MIN_CANDY_STEP and num <= max_step:
        return True
    else:
        return False


def computers_move(sum):
    max_step = MAX_CANDY_STEP
    if sum >= CNT_CANDY - MAX_CANDY_STEP:
        max_step = CNT_CANDY - sum

    return randint(MIN_CANDY_STEP, max_step)


def player_move(sum):
    max_step = MAX_CANDY_STEP
    if sum >= CNT_CANDY - MAX_CANDY_STEP:
        max_step = CNT_CANDY - sum
    num = int(
        input(f'Вы можете взять от {MIN_CANDY_STEP} до {max_step} конфет: '))
    check_input(num, max_step)

    while not check_input(num, max_step):
        num = int(
            input(f'Вы можете взять от {MIN_CANDY_STEP} до {max_step} конфет: '))
        check_input(num, max_step)

    return num


def get_first_move_player():
    return randint(1, CNT_PLAYERS)


def play_game(mode):
    num = 0

    id_player: int = get_first_move_player()
    computer_player: int = get_first_move_player()

    while num < CNT_CANDY:
        if mode == 'person':
            input_num = player_move(num)
        elif mode == 'computer':
            if id_player != computer_player:
                input_num = computers_move(num)
            else:
                input_num = player_move(num)

        num += input_num
        print(f'Взято конфет {num}')

        id_player = 1 if id_player == 2 else 2

    print(f"Победу одержал {PLAYERS_NAMES[1 if id_player == 2 else 2]}")


mode_num = int(input('Выберите режим (1 - с компьютером, 2 - с человеком): '))

if mode_num == 1:
    mode = MODE_1
if mode_num == 2:
    mode = MODE_2
mode = MODE_2

#move = randint(0, 1)
play_game(mode)
