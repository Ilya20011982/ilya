# Главный бухгалтер компании "Рога и копыта" случайно удалил ведомость с начисленной зарплатой. К счастью,
# у него сохранились расчётные листки всех сотрудников. Помогите по этим расчётным листкам восстановить зарплатную
# ведомость. Архив с расчётными листками доступен по ссылке
# https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip (вы можете скачать и распаковать его вручную
# или самостоятельно научиться делать это с помощью скрипта на Питоне).
# Ведомость должна содержать 1000 строк, в каждой строке должно быть указано ФИО сотрудника и, через пробел,
# его зарплата. Сотрудники должны быть упорядочены по алфавиту.

import requests
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile
import xlrd
import os

# url = 'https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip'
# req = requests.get(url)
# with req, ZipFile(BytesIO(req.content)) as archive:
#     archive.extractall('output')
test = os.listdir('output')
result = []
for item in test:
    wb = xlrd.open_workbook(f'output\\{str(item)}')
    sheet = wb.sheet_by_index(0)
    result.append((*sheet.row_values(1, 1, 2), int(*sheet.row_values(1, 3, 4))))
for j in sorted(result):
    print(*j)
