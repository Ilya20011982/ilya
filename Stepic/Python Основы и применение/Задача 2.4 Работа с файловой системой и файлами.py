# Вам дается текстовый файл, содержащий некоторое количество непустых строк.
# На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.
# Пример входного файла:
#     ab
#     c
#     dde
#     ff
# ﻿Пример выходного файла:
#     ff
#     dde
#     c
#     ab

with open('dataset_24465_4.txt') as f, open('text_out.txt', 'w') as w:
    text = f.readlines()
    text_out = [i for i in reversed(text)]
    w.writelines(text_out)