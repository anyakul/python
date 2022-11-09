from random import randint

MODE_1 = 'computer'
MODE_2 = 'person'
CNT_CANDY = 101
CNT_PLAYERS = 2
MIN_CANDY_STEP = 1
MAX_CANDY_STEP = 28

PLAYERS_NAMES = {
    1: 'Player_1',
    2: 'Player_2'
}

sum = 0


def computers_move(max_step):
    return randint(MIN_CANDY_STEP, max_step)


def get_max_step(num):
    res = MAX_CANDY_STEP

    if num >= CNT_CANDY - MAX_CANDY_STEP:
        res = CNT_CANDY - num

    return res
