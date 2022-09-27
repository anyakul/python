# 7) Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. (¬ отрицание, ∧ и, ∨ или)

def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def ifTruth(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result

statement = inputNumbers(3)

if ifTruth(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
