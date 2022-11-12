# 34) Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import func


def read_file(path):
    with open(path) as f:
        text = f.read()

    return text


def get_nums(data):
    numbers = []

    while data != '':
        if 'x^' in data:
            numbers.append(int(data[:data.index('x^')]))
            data = data[data.index('x^')+6:]
        elif 'x' in data:
            numbers.append(int((data[:data.index('x')])))
            data = data[data.index('x')+4:]
        else:
            numbers.append(int((data[:data.index(' ')])))
            data = data[data.index(' ')+5:]

    return numbers


def get_sum(poly1, poly2):
    lst = zip(poly1, poly2)
    res = []

    for el in lst:
        res.append(sum(list(el)))

    return res


str1 = read_file('gb_tasks/task034_GetSumPolynomials/file1.txt')
str2 = read_file('gb_tasks/task034_GetSumPolynomials/file2.txt')

lst1 = get_nums(str1)
lst2 = get_nums(str2)

res = get_sum(lst1[::-1], lst2[::-1])

func.write_file(func.create_str(res), 'task034_GetSumPolynomials/res.txt')
