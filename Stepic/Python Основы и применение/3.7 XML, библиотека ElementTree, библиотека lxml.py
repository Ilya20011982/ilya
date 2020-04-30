# Вам дано описание пирамиды из кубиков в формате XML.
# Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue).
# Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.
# Пример:
# <cube color="blue">
#   <cube color="red">
#     <cube color="green">
#     </cube>
#   </cube>
#   <cube color="red">
#   </cube>
# </cube>
# Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1.
# Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, имеют
# ценность 3. И т. д.
# Ценность цвета равна сумме ценностей всех кубиков этого цвета.
# Выведите через пробел три числа: ценности красного, зеленого и синего цветов.Sample
# Input:
# <cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>
#
# Sample Output:
# 4 3 1

import sys
from xml.etree import ElementTree


def all_cheked(tree, level, x='cube'):
    level += 1
    if not tree.findall(x):
        return
    else:
        for i in tree.findall(x):
            if colors.get(i.attrib['color']):
                colors[i.attrib['color']] += level
            else:
                colors[i.attrib['color']] = level
            all_cheked(i, level)
sys.stdin = open ('3.7 XML.txt')
level = 1
colors = {}
tree = ElementTree.fromstring(input())
colors[tree.attrib['color']] = level
all_cheked(tree, level)
for x in sorted(colors, reverse=True):
    print(colors[x], end=' ')


