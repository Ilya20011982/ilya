# В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: они говорили каким-то странным набором звуков.
# В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр, т.е. заменяли каждый 
# символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли ключ к шифру и теперь нуждаются в помощи:
# Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки одинаковой длины, 
# на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт строка, которую 
# нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.
# Пусть, например, на вход программе передано:
# abcd
# *d%#
# abacabadaba
# #*%*d*%
# Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
# Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки, которые 
# и передаём на вывод программы:
# *d*%*d*#*d*
# dacabac

def cipher(string, code, string_in_code):
    dict_cipher = {key: value for key, value in zip(string, code)}
    string_code = ''
    for i in string_in_code:
        string_code += dict_cipher[i]
    return string_code

def un_cipher(string, code, code_in_string):
    dict_cipher = {key: value for key, value in zip(code, string)}
    code_string = ''
    for i in code_in_string:
        code_string += dict_cipher[i]
    return code_string
 

string = input() 
code = input() 
string_in_code = input() 
code_in_string = input()
print(cipher(string, code, string_in_code))
print(un_cipher(string, code, code_in_string))