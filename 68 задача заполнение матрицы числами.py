# 68. *Заполните матрицу, содержащую N строк и M столбцов, натуральными числами по 
# спирали и змейкой:
# Вариант "В"
def print_matrix(matrix, lenght=5):
    for line in matrix:
        for item in line:
            print(f'{item:{lenght}}', end=' ')
        print()


lines, rows = map(int, input('Введите количество строк и столбцов: ').split())
matrix = [[0 for i in range(rows)] for j in range(lines)]
x = 0
for row in range(rows):
    if row % 2 != 0:
        for line in range(lines):
            matrix[-line - 1][row] = x + 1
            x += 1
    else:
        for line in range(lines):
            matrix[line][row] = x + 1
            x += 1
             
print_matrix(matrix)




