# 18) Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import func

with open('file.txt', 'w') as data:
    data.write(input('Номер строки: '))
    data.write(input('Номер строки: '))

data = open('file.txt', 'r')

#def mult_nums(my_list):
    #for line in data:
     #   print(line)


for line in data:
    print(line)

#count = int(input('Число чисел: '))
#max = int(input('Число max: '))
count = 5
max = 10

my_list = func.get_random(count, max)
print(my_list)
print(" ")
#mult_nums(my_list)
#print(result)