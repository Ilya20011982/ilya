from random import randint

n = 5
m = 7
with open('bug.txt', 'w') as f:
    f.write(str(n) + '\n')
    f.write(str(m) + '\n')
    for i in range(n):
        for j in range(m):
            f.write(str(randint(1, 10)) + ' ')
        f.write('\n')
