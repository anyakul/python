# Кортежи

a = (3, 4)
b = (3,) # кортеж из одного элемента
print(a)
print(a[0])
print(a[-1])

for item in a:
    print(item)

t = tuple(['red', 'green', 'blue'])
print(type(t))
red, green, blue = t
print('r: {} g: {} b: {}'.format(red, green, blue))
