# 37) Напишите программу, удаляющую из текста все слова, содержащие "abc".

def new_string(text):
    res = ''

    lst = text.split(' ')

    for i in lst:
        if 'abc' not in i:
            res += i + ' '

    return res

path = 'task037_DeleteWords/input_file.txt'
f = open(path, 'r')
text = f.read()
f.close()

res = new_string(text)
print(res)

with open('task037_DeleteWords/res.txt', 'w') as data:
    data.write(f'{res} \n')
f.close()
