# В римской системе счисления для обозначения чисел используются следующие символы (справа записаны числа, которым они
# соответствуют в десятичной системе счисления):
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
# Будем использовать вариант, в котором числа 4, 9, 40, 90, 400 и 900 записываются как вычитание из большего числа
# меньшего: IV, IX, XL, XC, CD и CM, соответственно.
# Напишите программу, которая переводит число из римской в десятичную систему счисления.
# Формат ввода:
# Строка, содержащая число, закодированное в римской системе счисления. Гарантируется, что число меньше 4000.
# Формат вывода:
# Строка, содержащая число в десятичной системе счисления, соответствующее введённому.


d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
x = input().upper().strip()
res = [d[x[0]]]
for i in x[1:]:
    if d[i] > res[-1]:
        res.append(d[i] - res.pop())
    else:
        res.append(d[i])
print(sum(res))
