
from collections import deque
r,c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(input())

visited = [[False]*c for _ in range(r)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]
ss = 0
ww = 0

def dfs(a,b):
    global ss, ww

    w = s = 0
    visited[a][b] = True
    q = deque([(a,b)])
    
    while q:
        x,y = q.popleft()
        
        if graph[x][y] == 'v':
            w += 1
        elif graph[x][y] == 'k':
            s += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if not visited[nx][ny] and graph[nx][ny] != '#':
                    visited[nx][ny] = True
                    q.append((nx,ny))
    
    if s > w:
        ss += s
    else:
        ww += w

for i in range(r):
    for j in range(c):
        if not visited[i][j] and graph[i][j] != '#':
            dfs(i,j)

print(ss, ww)

