# 3) Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

def get_numbers(n):
    list = []
    i = n * -1

    while i <= n:
        list.append(str(i))
        i += 1

    return list


num = int(input('Число: '))
list = get_numbers(num)
print(", ".join(list))
