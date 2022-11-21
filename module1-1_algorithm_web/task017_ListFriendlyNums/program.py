# 17) Два натуральных числа называют дружественными, если каждое из них равно сумме всех делителей другого, кроме самого этого числа. Найти все пары дружественных чисел, лежащих в диапазоне от 200 до 300


def get_multiples(num):
    lst = []

    for i in range(1, num - 1):
        if num % i == 0:
            lst.append(i)

    return lst


def get_res():
    for i in range(200, 300):
        for j in range(i + 1, 300):
            if i == sum(get_multiples(j)) and j == sum(get_multiples(i)):
                print(f'{i} {j}')


get_res()
