def get_multiplied_digits(number):
    str_number = str(abs(number))
    first = int(str_number[0])
    if str_number[-1] == '0':
        str_number = str_number[: -1]
    if len(str_number) <= 1:
        return first
    if len(str_number) >= 1:
        return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(40203) # ожидаемый ответ 24
print(result)
result2 = get_multiplied_digits(402030) # ожидаемый ответ 24
print(result2)