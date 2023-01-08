from collections import deque

r,c,n = map(int, input().split())
graph = []
for _ in range(r):
    tmp1 = input()
    tmp2 = []
    for t in tmp1:
        if t == '.':
            tmp2.append(0)
        else:
            tmp2.append(2)
    graph.append(tmp2)


dx = [0,0,-1,1]
dy = [-1,1,0,0]
if n == 1:
    pass
else:
    for _ in range(n-1):
        pop = []
        for i in range(r):
            for j in range(c):
                if graph[i][j] == 3:
                    pop.append((i,j))
                graph[i][j] += 1

        visited = [[False]*c for _ in range(r)]
        for x,y in pop:
            graph[x][y] = 0
            visited[x][y] = True

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        graph[nx][ny] = 0

for i in range(r):
    for j in range(c):
        if graph[i][j] == 0:
            print('.', end='')
        else:
            print('O', end='')
    print()
        
