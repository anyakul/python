# 23) Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import func

def get_multi(my_list):
    res = [];
    j = len(my_list) - 1
    list_len = len(my_list)
    res_len = list_len / 2

    if list_len % 2 == 1:
        res_len = res_len + 1

    for i in range(0, int(res_len)):
        res.append(my_list[i] * my_list[j])
        j -= 1

    return res

count = int(input('Количество чисел: '))
min = int(input('min: '))
max = int(input('max: '))
my_list = func.get_random(min, max, count)
print(my_list)
res = get_multi(my_list)
print()
print(res)
