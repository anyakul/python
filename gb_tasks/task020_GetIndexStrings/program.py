# 20) Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
str1 = "qwe"
list2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
str2 = "йцу"
list3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
str3 = "йцу"
list4 = ["123", "234", 123, "567"]
str4 = "123"
list5 = []
str5 = "йцу"


def get_index_string(lst, str):
    index = -1
    count = 0

    for i in range(len(lst)):
        if lst[i] == str:
            count += 1

            if (count == 2):
                index = i

    return index


print(" ")


res = get_index_string(list2, str2)

if res != -1:
    print(f"строка {str2} второй раз повторяется в индексе {res}")
else:
    print(f"Нет, строка {str2} не повторяется больше одного раза")
