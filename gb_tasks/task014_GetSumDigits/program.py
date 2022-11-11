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
    result = 0

    num = check_float(number)

    while num != 0:
        result += num % 10
        num = num // 10

    return result


number = input('Число n: ')
result = get_sum_digits(number)

print(f"Сумма цифр в числе {number} = {result}")
