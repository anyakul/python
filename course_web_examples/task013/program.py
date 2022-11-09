# 13) Дан список целых чисел. Подсчитать сколько четных чисел в списке

def count_even_nums(lst):
    count = 0

    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            count += 1

    return count


lst = [123, -34, 46, -567]
print(f'В списке {count_even_nums(lst)} чётных чисел')
