# 2) Даны действительные числа x и y. Получить (|x|-|y|)/(1+|x*y|)

x = float(input())
y = float(input())
res = (abs(x) - abs(y)) / (1 + abs(x * y))
print(res)
