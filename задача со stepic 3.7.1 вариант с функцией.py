# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и 
# выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков

def change_table(team, goal):
    if not team in table_result: table_result[team] = [0, 0, 0, 0, 0]
    table_result[team] = [table_result[team][0] + 1, 
                table_result[team][1] + 1 if goal == 3 else table_result[team][1],
                table_result[team][2] + 1 if goal == 1 else table_result[team][2],
                table_result[team][3] + 1 if goal == 0 else table_result[team][3],
                table_result[team][4] + goal,]  
table_result = {}
for i in range(int(input())):
    team_1, goal_1, team_2, goal_2 = input().split(';')    
    change_table(team_1, 3 if goal_1 > goal_2 else 1 if goal_1 == goal_2 else 0)
    change_table(team_2, 3 if goal_2 > goal_1 else 1 if goal_1 == goal_2 else 0)
for i, j in table_result.items():
    print(i + ':', *j, end='\n')