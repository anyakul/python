import json


def create(data):
    with open('task045_PhoneBook/index.json', 'w', encoding='utf-8') as outfile:
        outfile.write(json.dumps(data, ensure_ascii=False,
                      sort_keys=True, indent=4))
