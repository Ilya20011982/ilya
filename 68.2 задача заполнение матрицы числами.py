# 68. *Заполните матрицу, содержащую N строк и M столбцов, натуральными числами по 
# спирали и змейкой:
# Вариант "A"
def print_matrix(matrix, lenght=5):
    for line in matrix:
        for item in line:
            print(f'{item:{lenght}}', end=' ')
        print()


lines, rows = map(int, input('Введите количество строк и столбцов: ').split())
matrix = [[0 for i in range(rows)] for j in range(lines)]
x = 1
line = 0
row = 0

while matrix[line][row] == 0:
    
    for row in range(rows - 1):
        matrix[line][row] = x
        x += 1
    line +=1

    for line in range(lines - 1):
        matrix[line][rows - 1] = x
        x += 1

    for row in range(rows - 1):
        matrix[lines - 1][-row - 1] = x
        x += 1
        
    for line in range(lines - 1):
        matrix[-line - 1][row - row] = x
        x += 1
    
    row += 1
    lines -= 1
    rows -= 1
    print('line', line, 'row', row)



print('matrix')
print_matrix(matrix)
# print('line', line, 'row', row)
