# 38) Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


from random import randint

MODE_1 = 'computer'
MODE_2 = 'person'
CNT_CANDY = 100
CNT_PLAYERS = 2
MAX_CANDY_STEP = 28
MIN_CANDY_STEP = 0

PLAYERS_NAMES = {
    1: 'Player_1',
    2: 'Player_2'
}


def check_input(num):
    if num >= MIN_CANDY_STEP and num <= MAX_CANDY_STEP:
        return True
    else:
        return False


def computers_move():
    return randint(MIN_CANDY_STEP, MAX_CANDY_STEP)


def player_move():
    num = int(input(f'Вы можете взять от {MIN_CANDY_STEP} до {MAX_CANDY_STEP} конфет: '))
    check_input(num)
    while check_input(num) == False:
        num = int(input(f'Вы можете взять от {MIN_CANDY_STEP} до {MAX_CANDY_STEP} конфет: '))
        check_input(num)

    return num


def get_win(count_move):
    if count_move % 2 == 0:
        print('Выиграл второй игрок')
    else:
        print('Выиграл первый игрок')


def get_first_move_player():
    return randint(1, CNT_PLAYERS)


def play_game(mode, computer_move='no'):
    num = 0
    count_move = 0

    candy_players: dict = {
        1: 0,
        2: 0
    }

    id_player: int = get_first_move_player()
    computer_player: int = get_first_move_player()

    while num < CNT_CANDY:
        if mode == 'person':
            input_num = player_move()
        elif mode == 'computer':
            if id_player != computer_player:
                input_num = computers_move()
            else:
                input_num = player_move()

        candy_players[id_player] += int(input_num)
        num += candy_players[id_player]
        print(f'Взято конфет {num}')

        id_player = 1 if id_player == 2 else 2

    print(f"Победу одержал {PLAYERS_NAMES[1 if id_player == 2 else 2]}")


mode_num = int(input('Выберите режим (1 - с компьютером, 2 - с человеком): '))

if mode_num == 1:
    mode = MODE_1
if mode_num == 2:
    mode = MODE_2


move = randint(0, 1)
play_game(mode, move)
