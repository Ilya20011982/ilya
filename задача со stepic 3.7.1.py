# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и 
# выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков

n = int(input())
s = ''
z =[]
res = {}
while n > 0:
    s = input().split(';')
    z.append(s)
    s = ''
    n -= 1
print(z)
for j in z:
    if j[0] in res:
        res[j[0]][0] += 1
        if j[1] > j[3]:
            res[j[0]][1] += 1
            res[j[0]][4] += 3
        if j[1] < j[3]:
            res[j[0]][3] += 1
        if j[1] == j[3]:
            res[j[0]][2] += 1
            res[j[0]][4] += 1
    if j[2] in res:
        res[j[2]][0] += 1
        if j[1] < j[3]:
            res[j[2]][1] += 1
            res[j[2]][4] += 3
        if j[1] > j[3]:
            res[j[2]][3] += 1
        if j[1] == j[3]:
            res[j[2]][2] += 1
            res[j[2]][4] += 1
    if j[0] not in res: 
        if j[1] > j[3]:
            res[j[0]] = [1, 1, 0, 0, 3]
        if j[1] < j[3]:
            res[j[0]] = [1, 0, 0, 1, 0]
        if j[1] == j[3]:
            res[j[0]] = [1, 0, 1, 0, 1]
    if j[2] not in res:
        if j[1] > j[3]:
            res[j[2]] = [1, 0, 0, 1, 0]
        if j[1] < j[3]:
            res[j[2]] = [1, 1, 0, 0, 3]
        if j[1] == j[3]:
            res[j[2]] = [1, 0, 1, 0, 1]
for q, w in res.items():
    print((q + ':'), *w, end='\n')