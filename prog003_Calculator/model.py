signs = ["+", "-", "*", "/"]

rules = '''Калькулятор.
Доступные действия: сложение (+), вычитание(-), умножение(*) и деление(/). Знак = для вывода всего примера и результата. Чтобы начать заново наберите /start
Начальное число: 0. Введите число:
'''


def get_sign(current_lst):
    if len(current_lst) == 0:
        return "+"
    elif len(current_lst) > 0:
        return current_lst[len(current_lst) - 1]


def get_result(res, sign, num):
    if sign == '+':
        res += num
    elif sign == '-':
        res -= num
    elif sign == '*':
        res *= num
    elif sign == '/':
        res /= num

    return res
