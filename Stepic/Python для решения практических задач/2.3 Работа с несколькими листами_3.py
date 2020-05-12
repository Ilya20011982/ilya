# Вася составил раскладку по продуктам на весь поход (она на листе "Раскладка") с указанием номера дня, названия
# продукта и его количества в граммах. Для каждого дня посчитайте 4 числа: суммарную калорийность и граммы белков,
# жиров и углеводов. Числа округлите до целых вниз и введите через пробел. Информация о каждом дне должна выводиться
# в отдельной строке.

import xlrd

wb = xlrd.open_workbook('trekking3.xlsx')
sheet = wb.sheet_by_index(0)
sheet1 = wb.sheet_by_index(1)
vals = {str(*sheet.row_values(rownum, 0, 1 )): sheet.row_values(rownum, 1, sheet.nrows) for rownum in range(1, sheet.nrows)}
i = 1
day = 1
res = []
res_temp = [0, 0, 0, 0]
while i < sheet1.nrows:
    day_temp = int(*sheet1.row_values(i, 0, 1))
    if day_temp == day:
        for j in range(sheet.ncols-1):
            if vals[str(*sheet1.row_values(i, 1, 2))][j] == '':
                vals[str(*sheet1.row_values(i, 1, 2))][j] = 0
            res_temp[j] = res_temp[j] + vals[str(*sheet1.row_values(i, 1, 2))][j] * (float(*sheet1.row_values(i, 2, 3))/100)
    else:
        day = day_temp
        res += [res_temp]
        res_temp = [0, 0, 0, 0]
        for j in range(sheet.ncols-1):
            if vals[str(*sheet1.row_values(i, 1, 2))][j] == '':
                vals[str(*sheet1.row_values(i, 1, 2))][j] = 0
            res_temp[j] = res_temp[j] + vals[str(*sheet1.row_values(i, 1, 2))][j] * (float(*sheet1.row_values(i, 2, 3))/100)
    i += 1
res += [res_temp]
for i in res:
    for j in i:
        print(int(j), end=' ')
    print()
