# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
# Выведите одно число – количество вхождений строки t в строку s.
# Пример:
# s = "abababa"
# t = "aba"
# Вхождения строки t в строку s:
# abababa
# abababa
# abababa

s = input().lower()
t = input().lower()
count = 0
z = s
while len(t) <= len(s):
    if s.startswith(t):
        count += 1
    z = s[1:]
    s = z
print(count)
