# 23) Для каждого натурального числа в промежутке от m до n вывести все делители, кроме единицы и самого числа. m и n вводятся с клавиатуры.
# Пример:m =100, n = 105
# 100: 2 4 5 10 20 25 50
# 101:
# 102: 2 3 6 17 34 51
# 103:
# 104: 2 4 8 13 26 52
# 105: 3 5 7 15 21 35


def get_multiples(num):
    lst = []

    for i in range(2, num - 1):
        if num % i == 0:
            lst.append(i)

    return lst


def get_res(min_num, max_num):
    for i in range(min_num, max_num + 1):
        print(f'{i}: {get_multiples(i)}')


min_num = int(input('min: '))
max_num = int(input('max: '))
get_res(min_num, max_num)
