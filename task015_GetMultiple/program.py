# 15) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def get_multiple(number):
    result = []
    mult = 1

    for i in range(1, number + 1):
        mult *= i
        result.append(str(mult))
    
    return result

number = int(input('Число n: '))
result = get_multiple(number)
print(", ".join(result), end=".")
