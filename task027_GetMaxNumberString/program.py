# 27) Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

lst = [int(i) for i in input('Введите числа через пробел: ').split(" ")]

max_num = max(lst)
min_num = min(lst)

print(f"Минимальное число - {min_num}, максимальное - {max_num}")
