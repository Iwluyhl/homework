def print_params(a = 1, b = 'Строка', c = True):
    global values_list , values_list
    print(a, b, c)
    
print_params(3,5,6)
print_params(True)
print_params(b=25) # работает
print_params(c=[1, 2, 3]) # работает

values_list = [False, 2, "String"]
values_dict = {"a" : 10, "b": 'не строка', "c": None}

print_params(*values_list)
print_params(**values_dict)
