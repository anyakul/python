# 16) Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def get_list(n):
    result = []
    for el in range(1, n + 1):
        res = round(((1 + 1/el) ** el), 2)
        result.append(str(res))

    return result

def get_sum(list):
    sum = 0
    for el in list:
        sum += float(el)

    return sum

number = int(input('Число n: '))
list = get_list(number)
print(", ".join(list), end=".")
print(" ")
res = get_sum(list)
print(f"Сумма чисел = {res}")
