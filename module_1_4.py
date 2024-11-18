my_string = input("введите строку: ")
StringLen = len(my_string)
print("длина введеной строки: ", StringLen)
up = my_string.upper()
low = my_string.lower()
NoSpaces = my_string.replace(' ', '')
FirstChar = my_string[0]
LastChar =my_string[-1]
print("Строка в верхнем регистре: ", up)
print("Строка в нижнем регистре: ", low)
print("Строка без пробелов: ", NoSpaces)
print("Первый символ строки: ", FirstChar)
print("Последний символ строки: ", LastChar)
