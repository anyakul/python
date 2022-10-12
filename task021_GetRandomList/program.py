# 21) Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

from random import randint


def get_random(min, max, count):
    my_list = []

    for i in range(0, count):
        my_list.append(randint(min, max))

    return my_list


def get_random_new(min, max, count):
    return [randint(min, max) for i in range(0, count)]


count = int(input('Количество чисел: '))
min = int(input('min: '))
max = int(input('max: '))
my_list = get_random(min, max, count)
my_list_new = get_random_new(min, max, count)
print(my_list)
print(my_list_new)
