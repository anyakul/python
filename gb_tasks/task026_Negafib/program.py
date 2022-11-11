# 26) Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def multiply(x): return x * (-1)


def get_fib(num):
    result = []
    index = 0

    for i in range(num + 1):
        if i == 0 or i == 1:
            res = 1
        else:
            res = result[i - 2] + result[i - 1]
        result.append(res)
        index -= 1

    return result


def get_negafib(lst):
    return list(map(multiply, lst))


num = int(input('Число: '))

lst1 = get_fib(num)
lst2 = get_negafib(lst1)
lst2.reverse()
result = lst2 + lst1
print(result)
