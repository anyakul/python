from random import randint


def get_random(min_num, max_num, count):
    return [randint(min_num, max_num) for i in range(0, count)]
