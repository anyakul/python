import json


def read_file():
    with open('prog008_InfoSystem/data_file.json', 'r', encoding='utf8') as read_file:
        data = json.load(read_file)

    return data


def write_file(data):
    with open('prog008_InfoSystem/data_file.json', 'w', encoding='utf-8') as outfile:
        outfile.write(json.dumps(data, ensure_ascii=False,
                      sort_keys=True, indent=4))
