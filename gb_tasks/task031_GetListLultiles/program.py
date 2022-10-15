# 31) Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def get_multipliers(num):
    res = []
    i = 2

    while num > 1:
        if num % i == 0:
            res.append(i)
            num /= i
        else:
            i += 1

    return res


num = int(input('Число: '))
res = get_multipliers(num)
print(res)
