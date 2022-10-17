# 13) Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

def check_strings(string, substring):
    counter = 0

    for i in range(len(string) - len(substring) + 1):
        if string[i] == substring[0]:
            counterIn = 0

            for k in range(len(substring)):
                if substring[0+k] == string[i+k]:
                    counterIn += 1
            if counterIn == len(substring):
                counter += 1

    return counter


string = ''
substring = ''

str1 = input('Строка 1: ')
str2 = input('Строка 2: ')

if len(str1) > len(str2):
    string = str1
    substring = str2

else:
    string = str2
    substring = str1

result = check_strings(string, substring)
print(f"В строке {str2} {result} повторов строки {str1}")
