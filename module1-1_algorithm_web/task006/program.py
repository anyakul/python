# 6) Вводится с клавиатуры цена товара в копейках. Необходимо представить эту цену в виде X руб. XX коп.
# Например, вводится число 101. Необходимо вывести 1 руб. 01 коп.

a = int(input())
print(f"{int(a / 100)} руб {int(a % 100)} коп")
