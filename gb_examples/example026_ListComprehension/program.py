list1 = []

for i in range(1, 101):
    if i % 2 == 0:
        list1.append(i)

def f(x):
    return x ** 3

list2 = [i for i in range(1, 101) if i % 2 == 0]
list3 = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]

print(list1)
print(list2)
print(list3)
