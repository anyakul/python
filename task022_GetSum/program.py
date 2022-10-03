# 22) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import func


def get_sum(my_list):
    res = 0

    for i in range(0, len(my_list)):
        if i % 2 == 1:
            res = res + my_list[i]

    return res


count = int(input('Количество чисел: '))
min = int(input('min: '))
max = int(input('max: '))
my_list = func.get_random(min, max, count)
print(my_list)
res = get_sum(my_list)
print(f"Сумма чисел на нечётных позициях = {res}")
