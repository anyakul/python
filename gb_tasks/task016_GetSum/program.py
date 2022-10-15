# 16) Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму
# - Для n = 6: { 2.0, 2.25, 2.37, 2.44, 2.49, 2.52 }

def get_list(n):
    result = []
    for el in range(1, n + 1):
        num = round(((1 + 1/el) ** el), 2)
        result.append(str(num))

    return result


def get_sum(my_list):
    sum_num = 0
    for el in my_list:
        sum_num += float(el)

    return sum_num


number = int(input('Число n: '))
my_list = get_list(number)
print(", ".join(my_list), end=".")
print(" ")
res = get_sum(my_list)
print(f"Сумма чисел = {res}")
