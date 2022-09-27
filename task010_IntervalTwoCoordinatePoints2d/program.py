# 10) Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. 
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

def intervalPoints(x0, x1, y0, y1):
    return pow(x0 - x1, 2) + pow(y0 - y1, 2);

x0 = int(input(f"x0: "))
y0 = int(input(f"y0: "))
x1 = int(input(f"x1: "))
y1 = int(input(f"y1: "))

res = intervalPoints(x0, x1, y0, y1);

print(f"Расстояние между точками A({x0}, {y0}) и B ({x1}, {y1}) = {res}")
