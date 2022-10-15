def sum(x, y):
    return x + y


f = lambda x, y: x + y


def mylt(x, y):
    return x * y


m = lambda x, y: x * y


def calc(op, a, b):
    print(op(a, b))
    return (op(a, b))


calc(mylt, 4, 5)
calc(f, 4, 5)
calc(m, 4, 5)
