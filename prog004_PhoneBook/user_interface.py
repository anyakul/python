import data_provider as dt


def get_data():
    data = []
    print('ПРОГРАММА - СОЗДАНИЕ ТЕЛЕФОННОГО СПРАВОЧНИКА')
    point = int(input('Введите 1 чтобы ввести данные в телефонную книгу: '))

    while point == 1:
        one_data = {
            "first_name": dt.get_first_name(),
            "second_name": dt.get_second_name(),
            "phone_number": dt.get_phone_number(),
            "description": dt.get_description()
        }

        data.append(one_data)
        point = int(
            input('Введите 1 чтобы ввести новые данные, набирите 2 чтобы закончить ввод: '))

    return data
