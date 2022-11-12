# 22) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import func


def get_sum(lst):
    res = 0

    for i in range(1, len(lst), 2):
        res = res + lst[i]

    return res


count = int(input('Количество чисел: '))
min_num = int(input('min: '))
max_num = int(input('max: '))
lst = func.get_random(min_num, max_num, count)
print(lst)

result = get_sum(lst)
print(f"Сумма чисел на нечётных позициях = {result}")
