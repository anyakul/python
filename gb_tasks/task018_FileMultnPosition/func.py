from random import randint


def get_random(count, max):
    result = []
    min = max * -1

    for el in range(0, count + 1):
        result.append(randint(min, max))

    return result
