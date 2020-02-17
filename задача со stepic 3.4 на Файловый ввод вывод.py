# Напишите программу, которая считывает из файла строку, соответствующую тексту,
# сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
with open('in.txt', encoding='utf-8') as inf:
    text = inf.read()

text_out = ''
ch = ''
num = ''
for j in range(len(text) - 2):
    if not text[j].isdigit():
        ch = text[j]
    if text[j + 1].isdigit():
        num += text[j + 1]
    else:
        text_out += ch * (int(num) if num else 1)
        ch = ''
        num = ''

with open('out.txt', 'w', encoding='utf-8') as inf:
    inf.write(text_out)