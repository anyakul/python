# 41) Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# 1+2*3 => 7;
# (1+2)*3 => 9;


def polska(ex):
    stack_list = []
    result = []

    for el in ex:
        if el.isdigit():
            result.append(el)
        elif el == '(':
            stack_list.append(el)
        elif el == ')':
            while stack_list and stack_list[-1] != '(':
                result.append(stack_list.pop())
            stack_list.pop()
        elif el == "*" or el == "/":
            while stack_list and stack_list[-1] in ['*', '/']:
                result.append(stack_list.pop())
            stack_list.append(el)
        elif el == "+" or el == "-":
            while stack_list and stack_list[-1] in ['+', '-', '*', '/']:
                result.append(stack_list.pop())
            stack_list.append(el)

    while stack_list:
        result.append(stack_list.pop())

    return (result)


def get_res(ex):
    temp = []

    for i in ex:
        if i.isdigit():
            temp.append(int(i))
        elif i in ['+', '-', '*', '/']:
            b = temp.pop()
            a = temp.pop()
            if i == '+':
                temp.append(a+b)
            elif i == '-':
                temp.append(a-b)
            elif i == '*':
                temp.append(a*b)
            elif i == '/':
                temp.append(a/b)

    return temp


ex = '( 1 + 2 ) * 3'.split(' ')

res = polska(ex)
res = get_res(res)
print(res)
