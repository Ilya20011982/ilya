# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

import sys
import re
st = r'cat'
for line in sys.stdin:
    if line:
        line = line.rstrip()
        a = re.findall(st, line)
        if len(a) > 2:
            print(line)
        else:
            continue
    else:
        break
