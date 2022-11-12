# 2) Напишите программу, которая на вход принимает 5 чисел (можно списком) и находит максимальное из них.
# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90


def input_numbers(x):
    lst = []

    for i in range(x):
        lst.append(int(input("Введите значение: ")))

    return lst


count = int(input('Введите количество чисел в списке: '))
lst = input_numbers(count)
max_num = max(lst)

print(lst)
print(f'Максимальное число - {max_num}')
