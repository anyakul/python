# Списки: введение
# list = list

import numbers


numbers = [1, 2, 3, 4, 5]
print('numbers =',numbers)  #[1, 2, 3, 4, 5]
ran = range(1, 6)
print('type(ran) =', type(ran))
numbers = list(ran)  #[1, 2, 3, 4, 5]
print('numbers =', numbers)
print('len(numbers) =', len(numbers))
print('f{len(numbers)} =', f'{len(numbers)}')
numbers[0] = 10  #[10, 2, 3, 4, 5]
print('numbers =', numbers)

for i in numbers:
    i*= 2
    print('i =', i)  #[20, 4, 6, 8, 10]

print('numbers =', numbers)  #[1, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']

for e in colors:
    print(e)  # red green blue

for e in colors:
    print(e*2)  # redred greengreen blueblue

colors1 = colors.append('gray') # добавить в конце
print(colors == ['red', 'green', 'blue'])  # True
colors.remove('red') # удалить элемент
print(colors)
colors.remove(colors[0]) # удалить элемент
print(colors)

del colors[0]
print(colors)
