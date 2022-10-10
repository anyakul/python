# 37) Напишите программу, удаляющую из текста все слова, содержащие "абв".

def new_string(text):
    res = ''

    lst = text.split(' ')

    for i in lst:
        if 'абв' not in i:
            res += i + ' '

    return res


text = 'Напишите програбвмму, удаляющую из текстаабв всеабв слова, содержащие "абв".'
res = new_string(text)
print(res)
