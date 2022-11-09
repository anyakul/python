# 18) Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.

def get_sum(num):
    sum = 1

    for i in range(1, num):
        sum += 1/i

    return sum


num = int(input('Число:'))
print(get_sum(num))
