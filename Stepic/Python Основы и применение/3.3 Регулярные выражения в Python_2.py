# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве слова.

import sys
import re

st = r'\bcat\b'
for line in sys.stdin:
    if line:
        line = line.rstrip()
        a = re.search(st, line)
        if a:
            print(line)
        else:
            continue
    else:
        break
