# Вася планирует карьеру и переезд. Для это составил таблицу, в которой для каждого региона записал зарплаты для
# разных интересные ему профессий. Таблица доступна по ссылке
# https://stepik.org/media/attachments/lesson/245267/salaries.xlsx.
# Выведите название региона с самой высокой медианной зарплатой (медианой называется элемент, стоящий в
# середине массива после его упорядочивания) и, через пробел, название профессии с самой высокой средней
# зарплатой по всем регионам.

import xlrd, xlwt
from statistics import mean, median

wb = xlrd.open_workbook('salaries.xlsx')
sheet = wb.sheet_by_index(0)
max_solary = 0
i = 1
while i < sheet.nrows:
    solary = (median(sheet.row_values(i, 1, sheet.nrows)))
    if max_solary < solary:
        region = sheet.row_values(i, 0, 1)
        max_solary = solary
    i += 1

i = 1
max_solary = 0
while i < sheet.ncols:
    solary = mean(sheet.col_values(i, 1, sheet.ncols))
    if max_solary < solary:
        prof = sheet.col_values(i, 0, 1)
        max_solary = solary
    i += 1

print(*region, *prof)


