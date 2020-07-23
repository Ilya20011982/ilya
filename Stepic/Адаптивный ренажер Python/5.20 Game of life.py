# Напишите программу, вычисляющую следующее состояние поля для Game of life.
# Поле представляет собой прямоугольник, причём для крайних клеток поля соседними являются клетки с
# противоположного конца (поле представляет собой тор).
# Формат ввода:
# На первой строке указаны два целых числа через пробел -- высота и ширина поля.
# В следующих строках подаётся состояние поля. Точка "." обозначает мёртвую клетку, символ "X" − живую.
# Формат вывода:
# Следующее состояние поля, используя те же обозначения, что использовались на вводе.


def is_life(x, y):
    summ = 0
    for i in [-1, 0, 1]:
        if field[x - 1][(y + i) % m] == 'X':
            summ += 1
        if field[(x + 1) % n][(y + i) % m] == "X":
            summ += 1
    if field[x][(y + 1) % m] == "X":
        summ += 1
    if field[x][y - 1] == "X":
        summ += 1
    return summ


n, m = map(int, input().split())
field = [list(input()) for x in range(n)]
for i in range(n):
    for j in range(m):
        if field[i][j] == '.' and is_life(i, j) == 3:
            print('X', end='')
        elif field[i][j] == 'X' and (is_life(i, j) < 2 or is_life(i, j) > 3):
            print('.', end='')
        else:
            print(field[i][j], end='')
    print()

