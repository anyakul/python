# 8) Введите число. Если это число делиться на 1000 без остатка, то выведите на экран "millennium"


def check_num(num):
    num = int(input('Введите число: '))

    if num % 1000 == 0:
        print('millenium')


num = int(input('Введите число: '))
check_num(num)
