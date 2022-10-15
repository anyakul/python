# 42 Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


def get_single_nums(lst):
    res = []

    for i in range(0, len(lst)):
        if lst.count(lst[i]) == 1:
            res.append(lst[i])

    return res


lst = [int(i) for i in input('Введите числа через пробел: ').split(" ")]

result = get_single_nums(lst)
print(result)
