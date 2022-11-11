# 17) Реализуйте алгоритм перемешивания списка

from random import randint


def get_random(count, min_num, max_num):
    result = []

    for el in range(count + 1):
        result.append(randint(min_num, max_num))

    return result


def mix_list(lst):
    result = lst[:]

    for i in range(count + 1):
        index = randint(0, len(lst) - 1)
        temp = result[i]
        result[i] = result[index]
        result[index] = temp

    return result


count = int(input('Число чисел: '))
min_num = int(input('Число min: '))
max_num = int(input('Число max: '))

lst = get_random(count, min_num, max_num)
print(lst)
result = mix_list(lst)
print(result)
