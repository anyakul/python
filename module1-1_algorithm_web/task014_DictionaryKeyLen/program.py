# 14) Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}). Чтобы получить список ключей - использовать метод .keys()
# (подсказка: создается новый ключ с цифрой в конце, старый удаляется)


def get_key_len(dict):
    keys_lst = list(dict.keys())

    for i in range(len(keys_lst)):
        new_key = f'{keys_lst[i]}{len(keys_lst[i])}'
        dict[new_key] = dict[keys_lst[i]]
        del dict[keys_lst[i]]

    return dict


dict = {
    'test': 'test_value',
    'europe': 'eur',
    'dollar': 'usd',
    'ruble': 'rub'
}

print(get_key_len(dict))
