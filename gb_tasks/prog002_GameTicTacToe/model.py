# 39) Создайте программу для игры в "Крестики-нолики".

from model import *
from spy_log import *
from random import randint

X = 'X'
O = '0'
MODE_1 = 'computer'
MODE_2 = 'person'

nums = {1: 1, 2: 2, 3: 3, '\n': '\n', 4: 4,
        5: 5, 6: 6, '\nn': '\n', 7: 7, 8: 8, 9: 9}


def show_field(nums):
    return ' '.join('{}'.format(val) for key, val in nums.items())


def reset_nums(nums):
    for key, val in nums.items():
        if key != '\nn':
            nums[key] = key


def check_win(nums):
    if (nums[1] == nums[2] == nums[3]) or \
        (nums[4] == nums[5] == nums[6]) or \
        (nums[7] == nums[8] == nums[9]) or \
        (nums[1] == nums[4] == nums[7]) or \
        (nums[2] == nums[5] == nums[8]) or \
        (nums[3] == nums[6] == nums[9]) or \
        (nums[1] == nums[5] == nums[9]) or \
            (nums[3] == nums[5] == nums[7]):
        return True
    else:
        return False


def check_draw(nums):
    count_move = 0
    for key, value in nums.items():
        if nums[key] == X or nums[key] == O:
            count_move += 1
    if count_move == 9 and not check_win(nums):
        return True
    else:
        return False


def check_input(nums, num):
    if num < 1 and num > 10:
        return False
    elif nums[num] == X or nums[num] == O:
        return False
    else:
        return True


def computers_move(nums):
    num = randint(1, 9)
    check_input(nums, num)

    while not check_input(nums, num):
        num = randint(1, 9)
        check_input(nums, num)

    return num


def get_res_str(nums, id_player):
    if check_win(nums):
        return f'Выиграл {id_player}. Наберите /start чтобы играть снова'
    elif check_draw(nums):
        return 'Ничья. Наберите /start чтобы играть снова'


def get_first_move():
    num = randint(1, 2)

    if num == 1:
        return X
    if num == 2:
        return O


def get_computer_move(player_move):
    if player_move == X:
        return O
    elif player_move == O:
        return X
