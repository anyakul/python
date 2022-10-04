# 17) Реализуйте алгоритм перемешивания списка

from random import randint


def get_random(count, min, max):
    result = []
    for el in range(0, count + 1):
        result.append(str(randint(min, max)))

    return result


def mix_list(my_list):
    result = my_list[:]
    for i in range(count + 1):
        index = randint(0, len(my_list) - 1)
        temp = result[i]
        result[i] = result[index]
        result[index] = temp

    return result


count = int(input('Число чисел: '))
min = int(input('Число min: '))
max = int(input('Число max: '))

my_list = get_random(count, min, max)
print(", ".join(my_list), end=". ")
print(" ")
result = mix_list(my_list)
print(", ".join(result), end=".")
