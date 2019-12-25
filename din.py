fib = [1, 1]

for i in range(3, 50):
    fib.append(fib[-1] + fib[-2])

print(*fib, sep='\n')
