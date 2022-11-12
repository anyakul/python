# 8) Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0, и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

def get_quarter_coordinate(x, y):
    if x > 0 and y > 0:
        print("1 четверть")
    elif x < 0 and y > 0:
        print("2 четверть")
    elif x < 0 and y < 0:
        print("3 четверть")
    elif x > 0 and y < 0:
        print("4 четверть")
    else:
        print("На оси")


x = int(input(f"x: "))
y = int(input(f"y: "))
get_quarter_coordinate(x, y)
