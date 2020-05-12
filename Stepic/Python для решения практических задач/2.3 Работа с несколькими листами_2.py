# Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно, составив справочник продуктов
# с указанием калорийности на 100 грамм, а также содержание белков, жиров и углеводов на 100 грамм продукта. Ему не
# удалось найти всю информацию, поэтому некоторые ячейки остались незаполненными (можно считать их значение равным нулю).
# Также он использовал какой-то странный офисный пакет и разделял целую и дробную часть чисел запятой. Таблица доступна
# по ссылке https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx
# Вася составил раскладку по продуктам на один день (она на листе "Раскладка") с указанием названия продукта и
# его количества в граммах. Посчитайте 4 числа: суммарную калорийность и граммы белков, жиров и углеводов.
# Числа округлите до целых вниз и введите через пробел.

import xlrd

wb = xlrd.open_workbook('trekking2.xlsx')
sheet = wb.sheet_by_index(0)
sheet1 = wb.sheet_by_index(1)

vals = {str(*sheet.row_values(rownum, 0, 1 )): sheet.row_values(rownum, 1, sheet.nrows) for rownum in range(1, sheet.nrows)}
i = 1
res = [0, 0, 0, 0]
while i < sheet1.nrows:
    for j in range(sheet.ncols-1):
        if vals[str(*sheet1.row_values(i, 0, 1))][j] == '':
            vals[str(*sheet1.row_values(i, 0, 1))][j] = 0
        res[j] = res[j] + vals[str(*sheet1.row_values(i, 0, 1))][j] * (float(*sheet1.row_values(i, 1, 2))/100)
    i += 1
for i in res:
    print(int(i), end=' ')