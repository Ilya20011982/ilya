# 68. *Заполните матрицу, содержащую N строк и M столбцов, натуральными числами по 
# спирали и змейкой:
# Вариант "A"
def print_matrix(matrix, lenght=5):
    for line in matrix:
        for item in line:
            print(f'{item:{lenght}}', end=' ')
        print()


lines, rows = map(int, input('Введите количество строк и столбцов: ').split())
n = lines * rows
matrix = [[0 for i in range(rows)] for j in range(lines)]
x = 1
line = 0
row = 0

while x <= n and line < lines and row < rows:
    
    for row_ in range(row, rows):
        matrix[line][row_] = x
        x += 1
    if x > n:
        break

    for line_ in range(line + 1, lines):
        matrix[line_][rows - 1] = x
        x += 1
    if x > n:
        break
    
    for row_ in reversed(range(row, rows - 1)):
        matrix[lines - 1][row_] = x
        x += 1
    if x > n:
        break
    
    for line_ in reversed(range(line + 1, lines - 1)):
        matrix[line_][row] = x
        x += 1
    if x > n:
        break
    
    line += 1
    row += 1
    lines -= 1
    rows -= 1
    print('line', line, 'row', row)



print('matrix')
print_matrix(matrix)
# print('line', line, 'row', row)
