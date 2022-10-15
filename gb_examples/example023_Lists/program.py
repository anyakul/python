# Списки

list1 = [1, 2, 3, 4, 5]
list2 = list1

print(list1) # [1, 2, 3, 4, 5]
print(list2) # [1, 2, 3, 4, 5]
print()

list1[0] = 123
list2[1] = 333

print(list1) # [123, 333, 3, 4, 5]
print(list2) # [123, 333, 3, 4, 5]
print()

print(len(list1)) # 5
list1.pop(3)
print(list1) # [123, 333, 3, 5]
print()

list1.insert(2, 56)
list1.append(79) 

print(list1) # [123, 333, 56, 3, 5, 79]
print(list2) # [123, 333, 56, 3, 5, 79]
