def print_matrix(matrix, lenght=5):
    for line in matrix:
        for item in line:
            print(f'{item:{lenght}}', end=' ')
        print()


lines, rows = map(int, input('Введите количество строк и столбцов: ').split())
n = lines * rows
matrix = [[0 for i in range(rows)] for j in range(lines)]


def dirs():
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    i = 0
    while True:
        yield d[i % 4]
        i += 1


cnt = 1
x = 0
y = 0
d = dirs()
dir_ = next(d)
while cnt <= n:
    matrix[x][y] = cnt
    if x + dir_[0] >= lines or x + dir_[0] < 0 or y + dir_[1] >= rows or y + dir_[1] < 0 or matrix[x + dir_[0]][y + dir_[1]]:
        dir_ = next(d)
    x += dir_[0]
    y += dir_[1]
    cnt += 1

print_matrix(matrix)