# 39) Создайте программу для игры в "Крестики-нолики".

from telegram import Update
from telegram.ext import CallbackContext
import datetime
from model import *
from spy_log import *
from random import randint


X = 'X'
O = '0'
MODE_1 = 'computer'
MODE_2 = 'person'


def show_field(nums):
    print(' '.join('{}'.format(val) for key, val in nums.items()))


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


def check_draw(nums, count_move):
    if count_move == 9 and check_win(nums) == False:
        return True
    else:
        return False


def check_input(nums, num):
    if num < 1 or num > 9 or nums[num] == X or nums[num] == O:
        return False
    else:
        return True


def computer_move():
    return randint(1, 9)


def player_move(move):
    return int(input(f'Введите незанятое число от 1 до 9 за {move}: '))


def get_num(id_player, computers_move):
    if id_player == computers_move:
        num = computer_move()
    else:
        num = player_move(id_player)

    return num


def do_move(nums, num, id_player, count_move):
    nums[num] = id_player

    if check_win(nums) == True:
        print(f'Выиграл {id_player}')
        id_player = 'no'
    elif check_draw(nums, count_move) == True:
        print("Ничья")
        id_player = 'no'
    else:
        id_player = X if id_player == O else O

    return id_player


def play_game(nums, computer_move):
    id_player = X
    count_move = 0
    check_win(nums)

    while check_win(nums) == False or check_draw(nums, count_move) == False:
        num = get_num(id_player, computer_move)

        if check_input(nums, num) == True:
            count_move += 1
            if do_move(nums, num, id_player, count_move) != 'no':
                id_player = do_move(nums, num, id_player, count_move)
                show_field(nums)
            else:
                show_field(nums)
                break
        else:
            num = get_num(id_player, computer_move)
            continue


nums = {1: 1, 2: 2, 3: 3, '\n': '\n', 4: 4, 5: 5, 6: 6, '\n': '\n', 7: 7, 8: 8, 9: 9}

show_field(nums)
