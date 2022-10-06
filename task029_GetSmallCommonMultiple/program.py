# 29) Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# один из часто используемых в математике способов — это нахождение НОК при помощи разложения чисел на простые множители. В общем случае алгоритм будет выглядеть следующим образом:
# разложить оба числа на простые множители;
# выбрать одну группу множителей;
# добавить к ним множители из второй группы, которые отсутствуют в выбранной;
# найти их произведение.


def get_multiples(num):
    lst = []

    if num < 2:
        lst.append(1)

    for i in range(2, num+1):
        if num % i == 0:
            lst.append(i)

    return lst


def get_common_multiple(lst1, lst2):
    res = []

    if lst1[0] == 1 or lst2[0] == 1:
        res.append(1)

    else:
        for i in lst1:
            for j in lst2:
                if i == j:
                    res.append(i)

    if len(res) == 0:
        res.append(1)

    return res


def get_small_common_multiple(lst):
    min_num = lst[0]
    for i in lst:
        if i < min_num:
            min_num = i

    return min_num


num1 = int(input('число 1: '))
num2 = int(input('число 2: '))

lst1 = get_multiples(num1)
lst2 = get_multiples(num2)

common_lst = get_common_multiple(lst1, lst2)

res = get_small_common_multiple(common_lst)

print(f"Наименьший общий знаменатель чисел {num1} и {num2} = {res}")
