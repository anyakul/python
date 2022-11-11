import random


def get_random(min_num, max_num, count):
    return [round(random.uniform(min_num, max_num), 2) for i in range(0, count)]
