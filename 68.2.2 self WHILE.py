n = int(input())
matr = [[0 for i in range(n)] for j in range(n)]
cnt = n * n
k = 1
i,j = 0,0
while k <= cnt:
    widht, heigth = n - 1, n - 1    
    while widht > 0 and k <= cnt or n == 1 and k <= cnt:
        matr[i][j] = k
        k += 1
        j +=1
        widht -= 1
    while heigth > 0 and k <= cnt:
        matr[i][j] = k
        k += 1
        i += 1
        heigth -= 1
    widht, heigth = n - 1, n - 1
    while widht > 0 and k <= cnt:
        matr[i][j] = k
        widht -= 1        
        k += 1
        j -= 1
    while heigth > 0 and k <= cnt:
        matr[i][j] = k
        k += 1
        i -= 1
        heigth -= 1
    n = n - 2
    j += 1
    i += 1
for k in matr:
    for m in k:
        print(m, end=' ')
    print()