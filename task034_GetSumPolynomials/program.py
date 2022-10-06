# 34) Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import func


def read_file(file):
    with open(file, 'r') as data:
        for line in data:
            return line


def get_sum(poly1, poly2):
    lst = zip(poly1, poly2)
    res = []
    for el in lst:
        res.append(sum(list(el)))

    return res


k = int(input('Коэффициент: '))
koef1 = func.create_lst(k)
koef2 = func.create_lst(k)
res = get_sum(koef1, koef2)

func.write_file(func.create_str(koef1), 'task034_GetSumPolynomials/file1.txt')
func.write_file(func.create_str(koef2), 'task034_GetSumPolynomials/file2.txt')

func.write_file(func.create_str(res), 'task034_GetSumPolynomials/res.txt')
