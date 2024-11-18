immutableVar = ("a", 123, 3.14159, True)
print("Неизменяемый объект:", immutableVar)

try:
    immutableVar[0] = "b"
except TypeError as e:
    print("Ошибка:", e)

mutableList = ["apple", "banana", "cherry"]
print("Изменяемый объект перед изменением:", mutableList)
mutableList[0] = "pineapple"
print("Изменённый список:", mutableList)