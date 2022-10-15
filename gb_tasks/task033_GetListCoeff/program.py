# 33) Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def write_file(st):
    with open('gb_tasks/task033_GetListCoeff/file.txt', 'w') as data:
        data.write(st)


def get_random():
    return random.randint(0, 101)


def create_lst(k):
    return [get_random() for i in range(k+1)]


def create_str(sp):
    lst = sp[::-1]
    res_str = ''

    if len(lst) < 1:
        res_str = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                res_str += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    res_str += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                res_str += f'{lst[i]}x'
                if lst[i+1] != 0:
                    res_str += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                res_str += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                res_str += ' = 0'
    return res_str


k = int(input("Натуральная степень k = "))
koef = create_lst(k)
write_file(create_str(koef))
