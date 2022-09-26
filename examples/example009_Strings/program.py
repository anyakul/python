# строки

text = 'съешь ещё этих мягких французских булок'

print(len(text))  # 39
print("'ещё' in text", 'ещё' in text)  # true
print("isdigit", text.isdigit())  # false
print("islower", text.islower())  # true
print("replace", text.replace('ЕЩЁ', 'ещё'))
print('text[0]', text[0])  # с
# print('text[len(text)]', text[len(text)])  # IndexError
print('text[len(text) - 1]', text[len(text) - 1])  # к
print('text[-5]', text[-5])  # б
print('text[:]', text[:])  # print(text)
print('text[len(text) - 2:]', text[len(text) - 2:])  # ок
print('text[2:9]', text[2:9])  # ешь ещё
print('text[2:-18]', text[2:-18])  # ешь ещё этих мягких
print('text[0:len(text):6]', text[0:len(text):6])  # сеикакл
print('text[::6]', text[::6])  # сеикакл
help(text.istitle)

for c in text:
    print(c)
