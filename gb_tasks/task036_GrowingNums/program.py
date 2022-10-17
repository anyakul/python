# 36) Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


def get_growing_nums(lst):
    res = []
    count = 0
    res.append(lst[count])

    for i in lst:
        if i > res[count]:
            res.append(i)
            count += 1

    return res


lst = [int(i) for i in input('Введите числа через пробел: ').split(" ")]

result = get_growing_nums(lst)
print(result)
