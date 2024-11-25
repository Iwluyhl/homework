myList = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i <len(myList):
    currentNumber = myList[i]
    if currentNumber >= 0:
        print(currentNumber)
    else:
        break
        
    i += 1