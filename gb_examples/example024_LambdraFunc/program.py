def f(x):
    return x ** 2

g = f
print(f(2))
print(g(2))
print(type(f))
print(type(g))
print(g(1))

def calc1(x):
    return x + 10


print(calc1(10))


def calc2(x):
    return x * 10

print(calc1(10))


def math(op, x):
    print(op(x))

math(calc1, 10)
math(calc2, 10)
