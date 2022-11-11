# 23) Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import func


def get_multi(lst):
    res = []
    j = len(lst) - 1
    lst_len = len(lst)
    res_len = lst_len / 2

    if lst_len % 2 == 1:
        res_len = res_len + 1

    for i in range(int(res_len)):
        res.append(lst[i] * lst[j])
        j -= 1

    return res


count = int(input('Количество чисел: '))
min_num = int(input('min: '))
max_num = int(input('max: '))
lst = func.get_random(min_num, max_num, count)
print(lst)

res = get_multi(lst)
print()
print(res)
