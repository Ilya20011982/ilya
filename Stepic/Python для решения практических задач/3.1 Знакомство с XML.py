# В OpenStreetMap XML встречаются теги node, которые соответствуют некоторым точкам на карте. Ноды могут не только
# обозначать какой-то точечный объект, но и входить в состав way (некоторой линии, возможно замкнутой) и не иметь
# собственных тегов. Для доступного по ссылке https://stepik.org/media/attachments/lesson/245678/map1.osm фрагмента
# карты посчитайте, сколько node имеет хотя бы один вложенный тэг tag, а сколько - не имеют. В качестве ответа введите
# два числа, разделённых пробелом.

import xmltodict

with open('map1.osm', 'r', encoding='utf8') as fin:
    xml = fin.read()
p, tag = 0, 0
parsedxml = xmltodict.parse(xml)
for node in parsedxml['osm']['node']:
    if 'tag' in node:
        tag += 1
    else:
        p += 1
print(tag, p)
