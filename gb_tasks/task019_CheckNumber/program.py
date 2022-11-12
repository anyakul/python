# 19) Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

import func


def check_num(lst, num):
    if num in lst:
        return True


count = int(input('Количество строк: '))
num = input('Искомое число: ')

lst = func.input_strings(count)
print(lst)

res = check_num(lst, num)

if res:
    print(f"Да, число {num} есть в списке")
else:
    print(f"Нет, числа {num} нет в списке")
