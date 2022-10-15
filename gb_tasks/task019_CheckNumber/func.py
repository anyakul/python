from random import randint


def input_strings(count):
    result = []

    for i in range(count):
        result.append(input(f"Введите значение: "))

    return result
