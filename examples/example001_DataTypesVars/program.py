# типы данных и переменная
# int

value = None
a = 123
b = 1.23
print('a = ', a)
print('b = ', b)
value = 12334
print('value - ', type(value))

s = 'hello world'
s1 = 'hello "world'
s2 = "hello /n world"
s3 = "hello 'world"
print('s =', s)
print('s1 =', s1)
print('s2 =', s2)
print('s3 =', s3)
print('s -', type(s))

print(a, b, s)
# print(a, ' - ', b, ' - ' s)
print('{} - {} - {}'.format(a, b, s))
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')

f = True
print('f = ', f)
print('f -', type(f))

list = [1, 2, 3]
list2 = ['1', 2, 'hello world', True]
print('list =', list)
print(type(list))
print(list2)
