# 30) Вычислить число c заданной точностью d
# при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$
# Можно округлить пи из math, там точность 15 знаков

from math import pi


def calc_factor(num):
    result = 0

    while num % 1 > 0:
        num *= 10
        result += 1

    return result


accurancy = float(input('Введите необходимую точность: '))
res = round(pi, calc_factor(accurancy))

print(res)
