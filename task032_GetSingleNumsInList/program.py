# 32) Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def get_single_nums(lst):
    res = []

    for i in range(0, len(lst)):
        if lst.count(lst[i]) == 1:
            res.append(lst[i])

    return res


lst = [int(i) for i in input('Введите числа через пробел: ').split(" ")]

res = get_single_nums(lst)
print(res)

res = set(lst)
print(res)
