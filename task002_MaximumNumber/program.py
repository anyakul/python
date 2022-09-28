# 2) Напишите программу, которая на вход принимает 5 чисел (можно списком) и находит максимальное из них.
# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

def input_numbers(x):
    a = [x]

    for i in range(x):
        a.append(int(input(f"Введите значение: ")))

    return a

def get_maximum(list):
    max = list[0]

    for i in list:
        if i > max:
            max = i

    return max

count = int(input('Введите количество чисел в списке: '))
list = input_numbers(count)

max = get_maximum(list)

print(list)

print(f'Максимальное число - {max}');
