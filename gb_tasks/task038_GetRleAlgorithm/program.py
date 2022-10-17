# 40) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Кодирование длин серий (англ. run-length encoding, RLE) или кодирование повторов — алгоритм сжатия данных, заменяющий повторяющиеся символы (серии) на один символ и число его повторов. Серией называется последовательность, состоящая из нескольких одинаковых символов.


path = 'gb_tasks/task040_GetRleAlgorithm/input_file.txt'
f = open(path, 'r')
data = f.read()


def get_compression():
    res = []
    r = None
    for d in data:
        if d != r:
            res.append(d)
            res.append(str(1))
            r = d
        else:
            res[-1] = str(int(res[-1]) + 1)
    res_str = "".join(res)
    return res_str


def get_recover(text):
    res = []
    for i in range(0, len(text)):
        if text[i].isdigit() == True:
            for j in range(0, int(text[i])):
                res.append(text[i - 1])

    res_str = "".join(res)
    return res_str


res1 = get_compression()
res2 = get_recover(res1)

with open('gb_tasks/task040_GetRleAlgorithm/res.txt', 'w') as data:
    data.write(f'{res1} \n')
    data.write(res2 + '\n')
