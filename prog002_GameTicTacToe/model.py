# 39) Создайте программу для игры в "Крестики-нолики".

from model import *
from spy_log import *

X = 'X'
O = '0'

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
    count = 0
    for i in nums:
        if nums[i] == 'x' or nums[i] == 'o':
            count += 1
    if count == 9 and check_win(nums) == False:
        return True
    else:
        return False
