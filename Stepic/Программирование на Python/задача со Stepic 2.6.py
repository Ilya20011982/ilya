# Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой,
# содержащей только строку "end" (без кавычек) Программа должна вывести матрицу того же размера, у которой каждый элемент
# в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
# У крайних символов соседний элемент находится с противоположной стороны матрицы.
# В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.


x = []
cnt = 0
while True:
    s = input()
    if s == 'end':
        break
    else:
        n = [int(i) for i in s.split()]
        cnt = len(n)
    x.append(n)

for i in range(len(x)):
    for j in range(cnt):
        k = x[i - len(x) + 1][j] + x[i - 1][j] + x[i][j - cnt + 1] + x[i][j - 1]
        print(k, end=' ')
    print()
