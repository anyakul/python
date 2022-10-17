# 18) Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import func

with open('file.txt', 'w') as data:
    data.write(input('Номер строки: '))
    data.write(input('Номер строки: '))

data = open('file.txt', 'r')


for line in data:
    print(line)

count = 5
max_num = 10

my_list = func.get_random(count, max_num)
print(my_list)
print(" ")
