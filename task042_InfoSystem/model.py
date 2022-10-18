import json_model as jm


def search_user_data(data):
    index = -1
    search_string = input('Что ищете: ')
    cur_ind = 0

    for i in range(len(data)):
        for val in data[i].values():
            if val == search_string:
                index = cur_ind
                print(data[index])
                break
        cur_ind += 1
    if index == -1:
        print('Не найдено. Попробуйте ещё: ')

    return index


def add_new_key(data):
    user = input('Введите название нового поля: ')

    for x in data:
        x[user] = '*'

    return data


def delete_key(data):
    key = input('Введите название поля которое хотите удалить: ')

    for el in data:
        el.pop(key)

    return data


def add_new_user(data):
    keys = data[0].keys()

    user_data = {
        'id': len(data)
    }

    for key in keys:
        user_data[key] = input(key + ' ')

    data.append(user_data)


def change_user_data(data):
    index = search_user_data(data)
    change_key = input('Укажите какое значение хотели бы поменять: ')

    data[index][change_key] = input('Введите значение: ')


def delete_user_data(data):
    index = search_user_data
    answer = input('Вы действительно хотите удалить эту запись (да или нет)?')

    if answer == 'да':
        data.pop(index)
        print('Запись была удалена')
    else:
        print('Запись не удалена')


def save_data_in_file(data):
    jm.write_file(data)
