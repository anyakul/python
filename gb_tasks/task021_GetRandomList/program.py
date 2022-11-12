# 21) Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

from random import randint


def get_random(min_num, max_num, count):
    lst = []

    for i in range(0, count):
        lst.append(randint(min_num, max_num))

    return lst


def get_random_new(min_num, max_num, count):
    return [randint(min_num, max_num) for i in range(0, count)]


count = int(input('Количество чисел: '))
min_num = int(input('min: '))
max_num = int(input('max: '))
result = get_random(min_num, max_num, count)
result_new = get_random_new(min_num, max_num, count)
print(result)
print(result_new)
