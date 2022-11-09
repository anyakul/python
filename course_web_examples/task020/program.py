# 20) Задан целочисленный массив. Определить количество участков массива, на котором элементы монотонно возрастают (каждое следующее число больше предыдущего).


def get_new_lst(lst):
    count = 1

    for i in range(len(lst) - 1):
        if lst[i] <= lst[i+1]:
            continue
        else:
            count += 1

    return count


lst = [1, 2, 3, 1, 5, 2, 2, 6]
print(get_new_lst(lst))
