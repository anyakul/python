# 25) Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# 45 -> 101101
# 3 -> 11
# 2 -> 10


def get_num_binary(num):
    result = ''

    while num > 0:
        result += str(num % 2)
        num //= 2

    return result


num = int(input('Число: '))
res = int(str(get_num_binary(num))[::-1])

print(f"Число {num} в двоичной системе = {res}")
