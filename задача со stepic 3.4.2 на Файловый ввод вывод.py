# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое 
# слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое 
# (можно использовать оператор < для строк).
# В качестве ответа укажите вывод программы, а не саму программу.
# Слова, написанные в разных регистрах, считаются одинаковыми.

with open('in.txt', encoding='utf-8') as inf:
    text = []
    for line in inf:
        text += line.split()
    print(text)
    cnt, cnt_tmp = 0, 0
    value, value_tmp = '', ''
    while text:
        k = len(text)
        i = 0
        value_tmp = text[i]
        cnt_tmp += 1
        i += 1
        k -= 1
        while k > 0 :            
            if value_tmp.lower() == text[i].lower():
                cnt_tmp += 1
                k -= 1
                text.pop(i)
            else:
                i += 1
                k -= 1
        if cnt:
            if cnt < cnt_tmp:
                value = value_tmp
                text.pop(0) 
                cnt = cnt_tmp
                cnt_tmp = 0
            elif cnt == cnt_tmp:
                if value < value_tmp:
                    text.pop(0)
                    cnt_tmp = 0
                else:
                    value = value_tmp
                    text.pop(0)
                    cnt_tmp = 0
            else:
                text.pop(0) 
                cnt_tmp = 0
        else:
            value = value_tmp
            text.pop(0) 
            cnt = cnt_tmp
            cnt_tmp = 0
print(value, cnt)      