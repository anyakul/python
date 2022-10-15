# 35) В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.


def get_nums(data):
    nums = []

    while data != '':
        space_pos = data.index(' ')
        nums.append(int(data[:space_pos]))
        data = data[space_pos+1:]

    return nums


def get_num(lst):
    for i in range(len(lst)):
        if lst[i] + 1 != lst[i + 1]:
            return lst[i] + 1


path = 'gb_tasks/task035_GetMissedNum/file.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()

nums = get_nums(data)
print(nums)

result = get_num(nums)
print(f"Недостающее число - {result}")
