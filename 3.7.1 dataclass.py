import sys
sys.stdin = open('371.txt')


from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Team:
    victories: int = 0
    draw: int = 0
    fault: int = 0
    scores: int = 0

    def update(self, victories, draw, fault):
        self.victories += victories
        self.draw += draw
        self.fault += fault
        self.scores += victories * 3 + draw * 1


teams = defaultdict(Team)
for i in range(int(input())):
    t1, s1, t2, s2 = input().split(';')
    teams[t1].update(s1 > s2, s1 == s2, s1 < s2)
    teams[t2].update(s2 > s1, s2 == s1, s2 < s1)

for name, team in teams.items():
    print(f'{name}: {team.victories} {team.draw} {team.fault} {team.scores}')

sys.stdin.close()
