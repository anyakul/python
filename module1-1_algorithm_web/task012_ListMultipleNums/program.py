# 12) Дан список целых чисел.
# Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2


def get_new_list(lst):
    new_lst = []

    for i in range(len(lst)):
        new_lst.append(lst[i] * (-2))

    return new_lst


lst = [123, -34, 46, -567]
print(get_new_list(lst))
