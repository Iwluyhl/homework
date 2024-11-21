first = int(input())
second = int(input())
third = int(input())
setNumber = len({first, second, third})
if setNumber == 1:
    print(3)
elif setNumber == 2:
    print(2)
else:
    print(0)