# В файле https://stepik.org/media/attachments/lesson/209723/3.html находится одна таблица. Просуммируйте все числа в
# ней и введите в качестве ответа одно число - эту сумму. Для доступа к ячейкам используйте возможности BeautifulSoup.

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html') # скачиваем файл
html = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(html, 'html.parser') # делаем суп
summ = 0
for tr in soup.find_all('td'):
    summ += int(tr.text)
print(summ)
