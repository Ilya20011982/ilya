# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго
# с 2001 года по настоящее время.
# Одним из атрибутов преступления является его тип – Primary Type.
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

import csv


crimes = {}
with open("Crimes.csv") as f:
    text = csv.DictReader(f)
    for i in text:
        if '2015' in i['Date']:
            if crimes.get(i['Primary Type']):
                crimes[i['Primary Type']] += 1
            else:
                crimes[i['Primary Type']] = 1
max_value = max(crimes.values())
final_dict = {k: v for k, v in crimes.items() if v == max_value}
print(final_dict)
