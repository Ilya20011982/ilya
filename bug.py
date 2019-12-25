with open('bug.txt') as f:
    n = int(f.readline())
    m = int(f.readline())
    field = [[int(x) for x in line.split()] for line in f.readlines()]

result = [[0] * (m + 1)] + [[0] + line[:] for line in field]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        result[i][j] += max(result[i-1][j], result[i][j-1])

print(*result, sep='\n')

x = n - 1
y = m - 1
rout = []
while (x, y) != (0, 0):
    if result[x][y + 1] == result[x + 1][y + 1] - field[x][y]:
        rout.append('D')
        x -= 1
    else:
        rout.append('R')
        y -= 1

print(rout)