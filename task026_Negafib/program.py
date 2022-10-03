# 26) Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def get_negafib(num):
    my_list = []
    index = 0

    for i in range(0, num + 1):
        if index == 0:
            res = 0
        elif index == -1:
            res = 1
        else:
            res = ((-1) ** (i + 1)) * \
                (abs(my_list[i - 2]) + abs(my_list[i - 1]))
        my_list.append(res)
        index -= 1

    return my_list


def get_fib(my_list):
    res = []
    for el in my_list:
        if el != 0:
            res.append(abs(el))

    return res


num = int(input('Число: '))

res1 = get_negafib(num)
res2 = get_fib(res1)
res1.reverse()
res = res1 + res2
print(res)
