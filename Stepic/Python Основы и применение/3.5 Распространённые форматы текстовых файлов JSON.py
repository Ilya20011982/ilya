# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть
# поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.
# Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
# ﻿Эквивалент на Python:
# class A:
#     pass
# class B(A, C):
#     pass
# class C(A):
#     pass
# Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не
# наследуется явно от одного класса более одного раза.
# Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
# <имя класса> : <количество потомков>
# Выводить классы следует в лексикографическом порядке.

import json
import sys

sys.stdin = open('JSON.txt')
str = input()
data = json.loads(str)
number_of_children = {}


def cheked(x, data_chek):
    if number_of_children.get(x):
        number_of_children[x].add(x)
    else:
        number_of_children[x] = set([x])
    for i in data_chek:
        if number_of_children.get(i):
            number_of_children[i].add(x)
        else:
            number_of_children[i] = set([x])


def is_linked(child, parent):
    queue = [i for i in child]
    checked = set()
    while queue:
        el = queue.pop(0)
        if el in number_of_children and el not in checked:
            number_of_children[parent] = number_of_children[parent] | number_of_children[el]
            queue.extend(number_of_children[el])
            checked.add(el)


for i in data:
    cheked(i['name'], i['parents'])

for i in number_of_children:
    # print(number_of_children[i], i)
    is_linked(number_of_children[i], i)

for x in sorted(number_of_children.keys()):
    print(x, ':', len(number_of_children[x]))




