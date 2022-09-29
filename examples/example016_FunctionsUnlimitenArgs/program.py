# Функции с неограниченным количеством аргументов

def concatenatio(*params):
    res = ""
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w')) # asdw
