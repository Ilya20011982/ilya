# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
# Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.

import requests
with open('in.txt', encoding='utf-8') as inf:
    url = inf.readline().strip()
cnt = 1
while True:
    r = requests.get(url)
    print(r.text[0:2])
    if r.text[0:2] == 'We':
        print(r.url)
        with open(r.url, encoding='utf-8') as f:
            text = f.splitlines()
         with open('out.txt', 'w', encoding='utf-8') as inf:  # почему то ошибка при запросе r.url : Traceback (most recent call last):
                                                              #   File "1.py", line 10, in <module>
                                                              #     with open(r.url, encoding='utf-8') as f:
                                                              # OSError: [Errno 22] Invalid argument: 'https://stepic.org/media/
                                                              # attachments/course67/3.6.3/843785.txt'
            inf.write(''. join(text))
        break
    else:
        url = 'https://stepic.org/media/attachments/course67/3.6.3/' + r.text
        cnt += 1
        print('cnt =', cnt)
        print(url)