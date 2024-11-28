def get_matrix():

    n = int(input("Введите количество строк: "))
    m = int(input("Введите количество столбцов: "))
    value = input("Введите значение для заполнения матрицы: ")

    matrix = [[value] * m for _ in range(n)]
    
    return matrix

matrix = get_matrix()

for row in matrix:
    print(' '.join(row))