from random import randint

CNT_CANDY = 100
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

def get_first_move():
    return randint(1, 2)


def get_max_step(num):
    res = MAX_CANDY_STEP

    if num >= CNT_CANDY - MAX_CANDY_STEP:
        res = CNT_CANDY - num

    return res


def check_input(num, max_step):
    if num >= MIN_CANDY_STEP and num <= max_step:
        return True
    else:
        return False
