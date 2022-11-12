# 11) Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов. (умножаем на -3)
# Для N = 5: 1, -3, 9, -27, 81


def get_degree(number):
    result = []

    for degree in range(number + 1):
        result.append(str((-3)**degree))

    return result


def get_degree_new(number):
    li = [x for x in range(number + 1)]
    result = list(map(lambda x: (-3)**x, li))

    return result


number = int(input('Число n: '))
result = get_degree(number)

print(result)
print(get_degree_new(number))
