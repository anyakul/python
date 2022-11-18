# 26) Условие задания: напишите свой первый класс Triangle, в котором есть поля angle_1, angle_2, angle_3 и который при инициализации проверяет, что все введенные числа положительные и что сумма углов треугольника равна 180°.
# В случае, если треугольник может существовать, конструктор класса должен напечатать текст Triangle initialized, а если такой треугольник существовать не может, то Initialization failed.

from Triangle import Triangle

triangle_1 = Triangle(angle_1=3, angle_2=4, angle_3=5)
triangle_2 = Triangle(angle_1=3, angle_2=4, angle_3=7)
triangle_3 = Triangle(angle_1=3, angle_2=-4, angle_3=7)


def get_result(obj):
    if obj.check_nums():
        obj.check()
    else:
        print('Стороны прямоугольника должны быть положительными числами')


get_result(triangle_1)
get_result(triangle_2)
get_result(triangle_3)
