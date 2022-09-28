# 14) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
# 6782 -> 23
# 0.56 -> 11

def check_float(num):
    if num.find('.') != -1 and num.count('.') == 1:
        x = number.split(".")
        return int(x[0] + x[1])
    else:
        return int(num)

def get_sum_digits(number):
    sum = 0
    a = check_float(number)

    while a != 0:
        sum += a % 10
        a = a // 10

    return sum

number = input('Число n: ')
result = get_sum_digits(number)
print(f"Сумма цифр в числе {number} = {result}")
