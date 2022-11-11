# 12) Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


def get_index_value(number):
    result = {}

    for key in range(1, number + 1):
        result[key] = key * 3 + 1

    return result


number = int(input('Число n: '))
result = get_index_value(number)

print(result)
