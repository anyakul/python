# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

a = 1 > 4
b = 1 < 4 < 6
c = 'qwe'
d = 'qwe'
e = [1,2]
f = [1,2]
g = 1 > 2 or 4 < 6
is_odd = f[0] % 2 == 0

print('a =', a)
print('b ==', b)
print('c == d', c == d)
print('c == d', c == d)
print('g =', g)
print('f =', f)
print(2 in f)
print(not 2 in f)
print('is_odd =', is_odd)
