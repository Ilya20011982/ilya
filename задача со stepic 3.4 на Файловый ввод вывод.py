# Напишите программу, которая считывает из файла строку, соответствующую тексту, 
# сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
with open('in.txt', encoding='utf-8') as inf:
    text = inf.readlines()
    text_out = ''
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ch = ''
    num = ''
    for line in text:
        for j in range(len(line) - 2):
            if line[j] not in number:
                ch = line[j]
            if line[j + 1] in number:
                num += line[j + 1]
            if line[j + 2] not in number:
                text_out += ch * int(num)
                ch = ''
                num = ''
with open('out.txt', 'w', encoding='utf-8') as inf:
    inf.write(''. join(text_out))