# 3) Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5


def get_numbers(n):
    lst = []

    for i in range(-n, n + 1):
        lst.append(i)

    return lst


num = int(input('Число: '))
lst = get_numbers(num)

print(lst)
