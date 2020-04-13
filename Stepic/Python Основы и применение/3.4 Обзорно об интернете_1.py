# Рассмотрим два HTML-документа A и B.
# Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">,
# возможно с дополнительными параметрами внутри тега.
# Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один
# переход и из C в B можно перейти за один переход.
# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
# Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

import re
import requests

first_link = 'https://stepic.org/media/attachments/lesson/24472/sample0.html' #input()
second_link = 'https://stepic.org/media/attachments/lesson/24472/sample1.html' #input()

res = requests.get(first_link)
if res.status_code != 200:
    print('No')
else:
    pattern = r'href="(\S*)">\S*</a>'
    links = re.findall(pattern, res.text)
    all_links = []
    for line in links:
        tmp_link = requests.get(line)
        all_links += re.findall(pattern, tmp_link.text)
    if second_link in all_links:
        print('Yes')
    else:
        print('No')
