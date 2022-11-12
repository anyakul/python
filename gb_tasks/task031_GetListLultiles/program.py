# 31) Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def get_multipliers(num):
    res = []

    for i in range(2, num):
        if num % i == 0:
            res.append(i)

    return res


num = int(input('Число: '))
result = get_multipliers(num)

print(result)
