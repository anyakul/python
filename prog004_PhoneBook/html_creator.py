def create(data, device=1):
    html = '<html>\n <head></head>\n <body>\n'
    for el in data:
        html += '<p>Имя: {}</p>\n'\
            .format(el['first_name'])
        html += '  <p>Фамилия: {}</p>\n'\
            .format(el['second_name'])
        html += '  <p>Номер телефона: {}</p>\n'\
            .format(el['phone_number'])
        html += '  <p>Описание: {}</p>\n'\
            .format(el['description'])
        html += '  <div style="height: 16px"></div>\n'
    html += '</body>\n</html>'

    with open('task045_PhoneBook/index.html', 'w', encoding='utf-8') as page:
        page.write(html)
