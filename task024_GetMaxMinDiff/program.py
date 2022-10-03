# 24) Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import func

def get_diff(my_list):
    min = my_list[0]
    max = my_list[0]

    for i in range(0, int(len(my_list))):
        if my_list[i] > max:
            max = my_list[i]
        elif my_list[i] < min:
            min = my_list[i]

    return max - min

count = int(input('Количество чисел: '))
min = int(input('min: '))
max = int(input('max: '))

my_list = func.get_random(min, max, count)
print(my_list)
res = round(get_diff(my_list), 2)
print(f"Разница между минимальным и максимальныым числом = {res}")
