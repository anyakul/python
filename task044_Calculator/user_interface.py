import menu
import data_provider
import model


def get_operation(menu_point):
    if menu_point == 1:
        op = model.sum_nums
    elif menu_point == 2:
        op = model.substract_nums
    elif menu_point == 3:
        op = model.mult_nums
    elif menu_point == 4:
        op = model.divide_nums

    return op


def get_result():
    result = 0
    arr = []
    menu_point = menu.get_menu_point()

    while menu_point != 6 and menu_point != 5:
        if result == 0:
            num1 = data_provider.get_nums()
            num2 = data_provider.get_nums()
            arr.append(str(num1))
            sign = menu.get_sign(menu_point)
            arr.append(sign)
            arr.append(str(num2))
        else:
            num1 = result
            num2 = data_provider.get_nums()
            sign = menu.get_sign(menu_point)
            arr.append(sign)
            arr.append(str(num2))
        op = get_operation(menu_point)
        result = model.calc(op, num1, num2)
        print(result)
        menu_point = menu.get_menu_point()

    if menu_point == 5:
        res = " ".join(arr) + ' = ' + str(result)
        print(res)
    
    if menu_point == 6:
        print(result)
