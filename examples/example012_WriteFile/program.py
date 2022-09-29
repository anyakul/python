# Запись файлов

colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors) # разделителей не будет
data.write('\n LINE2 \n')
data.write('\n LINE3 \n')
data.close()

with open('file.txt', 'w') as data:
    data.write('line1 \n')
    data.write('line1 \n')
