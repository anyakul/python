from random import randint


def get_random(count, max_num):
    result = []
    min_num = max_num * -1

    for el in range(0, count + 1):
        result.append(randint(min_num, max_num))

    return result
