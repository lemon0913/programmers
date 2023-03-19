# 열심히 삽질하고 있었는데 파이썬 정규표현식 유형이란다...ㅎㅎ
# 문자열 공부 열심히 해야할듯

import re
p = re.compile('^[A-F]?A+F+C+[A-F]?$')

t = int(input())
for _ in range(t):
    s = input()
    if p.match(s) == None:
        print('Good')
    else:
        print('Infected!')
