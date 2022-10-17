# 19) Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

import func


def check_num(my_list, num):
    result = False

    for i in range(0, len(my_list)):
        if my_list[i] == num:
            result = True

    return result


count = int(input('Количество строк: '))
num = input('Искомое число: ')

my_list = func.input_strings(count)
print(my_list)
print(" ")

res = check_num(my_list, num)

if res:
    print(f"Да, число {num} есть в списке")
else:
    print(f"Нет, числа {num} нет в списке")
