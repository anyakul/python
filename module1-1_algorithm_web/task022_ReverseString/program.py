# 22) В заданной строке расположить в обратном порядке все слова. Разделителями слов считаются пробелы.


def get_new_string(str):
    lst = str.split(' ')
    lst.reverse()

    return " ".join(lst)


str = input('Введите строку:')
print(get_new_string(str))
