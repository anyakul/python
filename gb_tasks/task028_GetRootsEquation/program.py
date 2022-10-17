# 28) Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# с помощью математических формул нахождения корней квадратного уравнения
# с помощью дополнительных библиотек Python (например, numpy.roots)

import math
import numpy


def get_discriminant(a, b, c):
    return b * b - 4 * a * c


def get_roots(a, b, c):
    d = get_discriminant(a, b, c)

    if d < 0:
        print("Корней нет")
    elif d == 0:
        res = -(b / 2 * a)
        print(f"Корень уравнения = {res}")
    else:
        res1 = (-b + math.sqrt(d)) / (2 * a)
        res2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"Корни уравнения = {res1} и {res2}")


a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

get_roots(a, b, c)
print(numpy.roots([a, b, c]))
