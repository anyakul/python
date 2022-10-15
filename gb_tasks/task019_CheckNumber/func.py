from random import randint


def input_strings(x):
    result = []

    for i in range(x):
        result.append(input(f"Введите значение: "))

    return result
