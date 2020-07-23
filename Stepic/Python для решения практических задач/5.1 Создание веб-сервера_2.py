# В этой задаче вам необходимо научиться генерировать html-код на питоне и сдать на проверку html-файл, в котором будет
# таблица размером 10 на 10, которая должна содержать таблицу умножения для чисел от 1 до 10. При открытии вашего файла
# в браузере это должно выглядеть примерно так:
# В этой задаче вам необходимо научиться генерировать html-код на питоне и сдать на проверку html-файл, в котором
# будет таблица размером 10 на 10, которая должна содержать таблицу умножения для чисел от 1 до 10. При открытии
# вашего файла в браузере это должно выглядеть примерно так:

from yattag import Doc
from yattag import indent

doc, tag, text = Doc().tagtext()
table_my = [[i * j for i in range(1, 11)] for j in range(1, 11)]

with tag('html'):
    with tag('body'):
        with tag('table'):
            for x in range(1, 11):
                with tag('tr'):
                    for j in table_my[x - 1]:
                        with tag('td'):
                            with tag('a', href=f'http://{j}.ru'):
                                text(j)

result = indent(doc.getvalue())
with open('my_tale.html', 'w') as f:
    f.write(result)

