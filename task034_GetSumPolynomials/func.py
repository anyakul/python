import random


def write_file(st, file):
    with open(file, 'w') as data:
        data.write(st)


def get_random():
    return random.randint(0, 101)


def create_lst(k):
    lst = [get_random() for i in range(k+1)]
    return lst


def create_str(sp):
    lst = sp[::-1]
    str = ''
    if len(lst) < 1:
        str = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                str += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    str += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                str += f'{lst[i]}x'
                if lst[i+1] != 0:
                    str += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                str += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                str += ' = 0'
    return str
