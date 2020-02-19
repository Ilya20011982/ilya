hi = [0] * 12
cnt = [0] * 12
with open('375.txt') as f:
    for line in f:
        c, h = map(int, line.split()[::2])
        hi[c] += h
        cnt[c] += 1

for i in range(1, 12):
    if cnt[i]:
        print(i, hi[i] / cnt[i])
    else:
        print(i, '-')
