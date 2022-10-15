menu_points = {
    '+': '1. Сложение',
    '-': '2. Вычитание',
    '*': '3. Умножение',
    '/': '4. Деление',
    'log': '5. Лог событий',
    'result': '6. Вывод',
}


def get_menu_point():
    print('ПРОГРАММА - КАЛЬКУЛЯТОР')
    print(menu_points["+"])
    print(menu_points["-"])
    print(menu_points["*"])
    print(menu_points["/"])
    print(menu_points["log"])
    print(menu_points["result"])

    while True:
        try:
            point = int(input('Введите номер пункта меню: '))
            if point in [1, 2, 3, 4, 5, 6]:
                break
        except ValueError:
            print('Введён неправильный пункт меню. Попробуйте ещё раз')

    return point


def get_sign(menu_point):
    if menu_point == 1:
        return '+'
    elif menu_point == 2:
        return '-'
    elif menu_point == 3:
        return '*'
    elif menu_point == 4:
        return '/'
