# Файл https://stepik.org/media/attachments/lesson/209719/2.html содержит статью с Википедии про язык Python.
# В этой статье есть теги code, которыми выделяются конструкции на языке Python. Вам нужно найти все строки,
# содержащиеся между тегами <code> и </code> и найти те строки, которые встречаются чаще всего и вывести их
# в алфавитном порядке, разделяя пробелами.
# Например, если исходный текст страницы выглядел бы так:
# <code>a</code>
# <a>bracadabr</a>
# <code>c</code>
# <code>b</code>
# <code>b</code>
# <code>c</code>
# то в ответ надо было бы ввести строку "b c".

import re
import requests

text_list = re.findall("<code>(.*?)</code>", requests.get(' https://stepik.org/media/attachments/lesson/209719/2.html').text)
text = {}
for i in text_list:
    text[i] = text_list.count(i)
max_el = max(text.values())
res = [j for j,v in text.items() if max_el == v]
for i in sorted(res):
    print(i, end=" ")
