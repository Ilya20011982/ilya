# Вам дана последовательность строк.
# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
# Sample Input:
# blabla is a tandem repetition
# 123123 is good too
# go go
# aaa
# Sample Output:
# blabla is a tandem repetition
# 123123 is good too

import sys
import re

st = r'\b(\w+)\1\b)'
for line in sys.stdin:
    if line:
        line = line.rstrip()
        a = re.findall(st, line)
        if a:
            print(line)
        else:
            continue
    else:
        break
