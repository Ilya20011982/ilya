# Вася решил открыть АЗС (заправку). Чтобы оценить уровень конкуренции он хочет изучить количество заправок в
# интересующем его районе. Вася скачал интересующий его кусок карты OSM
# https://stepik.org/media/attachments/lesson/245681/map2.osm и хочет посчитать, сколько на нём отмечено точечных
# объектов (node), являющихся заправкой. В качестве ответа вам необходимо вывести одно число - количество АЗС.

import xmltodict

with open('map2.osm', 'r', encoding='utf8') as fin:
    xml = fin.read()
count = 0
parsedxml = xmltodict.parse(xml)
for some in parsedxml['osm']:
    if isinstance(parsedxml['osm'][some], list):
        for some_with_tag in parsedxml['osm'][some]:
            if 'tag' in some_with_tag:
                tags = some_with_tag['tag']
                if isinstance(tags, list):
                    for tag in tags:
                        if '@k' in tag and tag['@k'] == 'amenity' and tag['@v'] == 'fuel':
                              count += 1
                elif isinstance(tags, dict):
                    if tags['@v'] == 'fuel':
                        count += 1
print(count)
