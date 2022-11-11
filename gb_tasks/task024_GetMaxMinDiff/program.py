# 24) Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import func


def get_diff(lst):
    min_num = round(lst[0] % 1, 2)
    max_num = round(lst[0] % 1, 2)

    for i in range(int(len(lst))):
        if round(lst[i] % 1, 2) > max_num:
            max_num = round(lst[i] % 1, 2)
        elif round(lst[i] % 1, 2) < min_num:
            min_num = round(lst[i] % 1, 2)

    return max_num - min_num


count = int(input('Количество чисел: '))
min_num = int(input('min: '))
max_num = int(input('max: '))
lst = func.get_random(min_num, max_num, count)
print(lst)

res = round(get_diff(lst), 2)
print(
    f"Разница между минимальной и максимальной частью дробного числа = {res}")
