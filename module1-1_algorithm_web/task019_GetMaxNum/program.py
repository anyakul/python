# 19) В массиве целых чисел с количеством элементов 19 определить максимальное число и заменить им все четные по значению элементы.


def get_new_lst(lst):
    max_num = max(lst)

    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = max_num

    return lst


lst = [1, 2, 3, 4, 5]
print(get_new_lst(lst))
