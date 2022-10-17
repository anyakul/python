from random import randint


def get_random(min_num, max_num, count):
    lst = []

    for i in range(0, count):
        lst.append(randint(min_num, max_num))

    return lst
