import random


def get_random(min_num, max_num, count):
    lst = []

    for i in range(0, count):
        lst.append(round(random.uniform(min_num, max_num), 2))

    return lst
