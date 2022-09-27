# 3) Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

def inputNumbers(x):
    a = x * -1

    while a != x + 1:
        print(a)
        a = a + 1

num = int(input('Число: '))
inputNumbers(num)
