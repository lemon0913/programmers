# 지뢰가 있으면서 열린칸을 고려 안함
# 문제 제대로 읽자...

n = int(input())

pop = []
for _ in range(n):
  pop.append(list(input()))
l = len(pop[0])

now = []
for _ in range(n):
  now.append(list(input()))

result = [['.']*l for _ in range(n)]

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
flag = False
for j in range(l):
  for i in range(n):
    if now[i][j] == 'x':
      if pop[i][j] == '.':
        cnt = 0
        for k in range(8):
          nx = i + dx[k]
          ny = j + dy[k]
          if 0 <= nx < n and 0 <= ny < l:
            if pop[nx][ny] == '*':
              cnt += 1
  
        result[i][j] = str(cnt)
      else:
        flag = True

if flag:
  for j in range(l):
    for i in range(n):
      if pop[i][j] == '*':
        result[i][j] = '*'

for r in result:
  print(''.join(r))
