# 37) Напишите программу, удаляющую из текста все слова, содержащие "abc".


import codecs

def rm_pattern(usr_data: str, pattern: str) -> str:

    return ' '.join([word for word in usr_data.split() if not pattern in word])

PATTERN = 'абв'

path = 'task037_DeleteWords/input_file.txt'
f = codecs.open(path, 'r', encoding='utf-8')
my_text = f.read()
f.close()

res = rm_pattern(my_text, PATTERN)
print(res)

with codecs.open('task037_DeleteWords/res.txt', 'w', 'utf-16') as data:
    data.write(res + '\n')
f.close()
