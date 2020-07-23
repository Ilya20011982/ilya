# Условие задачи:
# Нужно узнать правильно ли расставлены скобки в строке. Если скобки в строке расставлены правильно,
# выведите строку “Success". В противном случае выведите индекс (используя индексацию с единицы) первой
# закрывающей скобки, для которой нет соответствующей открывающей. Если такой нет, выведите индекс первой
# открывающей скобки, для которой нет соответствующей закрывающей.
# Sample Input 1:
# ([](){([])})
# Sample Output 1:
# Success
# Sample Input 2:
# ()[]}
# Sample Output 2:
# 5
# Sample Input 3:
# {{[()]]
# Sample Output 3:
# 7

brackets = {'(': ')', '[': ']', '{': '}'}
bracket = [i for i in input()]
stack = []
for i, val in enumerate(bracket):
    if val in '()[]{}':
        if val in brackets:
            stack.append((i + 1, val))
        else:
            if stack:
                tmp = stack.pop()
                if brackets[tmp[-1]] == val:
                    tmp = ()
                else:
                    print(i + 1)
                    break
            else:
                print(i + 1)
                break
    else:
        continue
else:
    if stack:
        tmp = stack.pop()
        print(tmp[0])
    else:
        print('Success')








