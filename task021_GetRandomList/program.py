# 21) Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

from random import randint


def get_random(min_num, max_num, count):
    my_list = []

    for i in range(0, count):
        my_list.append(randint(min_num, max_num))

    return my_list


def get_random_new(min_num, max_num, count):
    return [randint(min_num, max_num) for i in range(0, count)]


count = int(input('Количество чисел: '))
min_num = int(input('min: '))
max_num = int(input('max: '))
my_list = get_random(min_num, max_num, count)
my_list_new = get_random_new(min_num, max_num, count)
print(my_list)
print(my_list_new)
