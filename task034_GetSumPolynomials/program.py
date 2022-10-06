# 34) Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import func

def read_file(file):
    with open(file, 'r') as data:
        for line in data:
            return line


def get_sum(poly1, poly2):
    res = []
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            if i == j:
                res_equal = poly1[i] + poly2[j]
        if res_equal != 0:
            res.append(res_equal)

    return res


str1 = read_file('task034_GetSumPolynomials/file1.txt')
str2 = read_file('task034_GetSumPolynomials/file2.txt')

k = 3
koef1 = func.create_lst(k)
koef2 = func.create_lst(k)
res = get_sum(koef1, koef2)
print(res)
func.write_file(func.create_str(koef1), 'task034_GetSumPolynomials/file1.txt')
func.write_file(func.create_str(koef2), 'task034_GetSumPolynomials/file2.txt')
func.write_file(func.create_str(res), 'task034_GetSumPolynomials/res.txt')
