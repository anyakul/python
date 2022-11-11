# 16) Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму
# - Для n = 6: { 2.0, 2.25, 2.37, 2.44, 2.49, 2.52 }


def get_list(n):
    result = []

    for el in range(1, n + 1):
        num = round(((1 + 1/el) ** el), 2)
        result.append(num)

    return result


number = int(input('Число n: '))
lst = get_list(number)

print(lst)
print(f"Сумма чисел = {sum(lst)}")
