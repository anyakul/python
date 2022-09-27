# 2) Напишите программу, которая на вход принимает 5 чисел (можно списком) и находит максимальное из них.
# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

from itertools import count


def inputNumbers(x):
    a = [x]
    for i in range(x):
        a.append(int(input(f"Введите значение: ")))
    return a

count = int(input('Введите количество чисел в списке: '))
list = inputNumbers(count)
max = list[0]
print(list)

for i in list:
    if i > max:
        max = i

print(f'Максимальное число - {max}');
