def find_password(n):
    password = ""
    for a in range(1, 21):
        for b in range(a, 21):
            if a + b == n and a!=b or n % (a+b) == 0 and a!=b:
                password += f"{a}{b}"
    return password

number = int(input("Введите число от 3 до 20: "))
result = find_password(number)
print(f"Пароль для числа {number}: {result}")