def get_multiplied_digits (number):
    str_number = str(abs(number))
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first
    
number = 40203
result = get_multiplied_digits(number)
print(f"Произведение цифр числа {number}: {result}")