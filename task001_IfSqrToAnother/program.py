# 1) Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# 5, 25 -> да
# 4, 16 -> да
# 25, 5 -> да
# 8,9 -> нет

a = int(input('Введите a: '))
b = int(input('Введите b: '))
print(f'Вы ввели числа {a} и {b}');

if a == b ** 2:
    print(f'Число {a} является квадратом числа {b}');
elif b == a ** 2:
    print(f'Число {b} является квадратом числа {a}');
else:
    print('Ни одно число не является квадратом другого');
