def create(data, device=1):
    xml = '<xml>\n'
    for el in data:
        xml += '<first_name>Имя: {}</first_name>\n'\
            .format(el['first_name'])
        xml += '<second_name>Фамилия: {}</second_name>\n'\
            .format(el['second_name'])
        xml += '<phone_number>Номер телефона: {}</phone_number>\n'\
            .format(el['phone_number'])
        xml += '<description>Описание: {}</description>\n'\
            .format(el['description'])
        xml += ' \n'
    xml += '</xml>'

    with open('task045_PhoneBook/index.xml', 'w', encoding='utf-8') as page:
        page.write(xml)

    return data
