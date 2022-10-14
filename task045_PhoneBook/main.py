# 45) Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах (например, csv, json, xml…).

import user_interface
import html_creator
import xml_creator
import json_creator

data = user_interface.get_data()
html_creator.create(data)
xml_creator.create(data)
json_creator.create(data)
