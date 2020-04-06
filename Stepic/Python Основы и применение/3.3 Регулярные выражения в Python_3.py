# Вам дана последовательность строк.
# Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
# Sample Input:
# zabcz
# zzz
# zzxzz
# zz
# zxz
# zzxzxxz
# Sample Output:
# zabcz
# zzxzz

import sys
import re

st = r'z.{3}z'
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
