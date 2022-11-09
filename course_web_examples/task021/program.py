# 21) Дана целочисленная квадратная матрица. Найти в каждой строке наибольший элемент и поменять его местами с элементом главной диагонали.

import numpy as np

matrix = [[1, 4, 5],
          [15, -12, 9],
          [-6, -2, -8]]


def get_max_nums():
    max_lst = []

    for row in matrix:
        max_lst.append(max(row))

    return max_lst


def get_new_matrix():
    lst = get_max_nums()
    i = 0

    for x in range(0, len(matrix)):
        matrix[x][x] = lst[i]
        i += 1

    return matrix


print(get_max_nums())
print(get_new_matrix())
