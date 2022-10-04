from collections import deque


M, N = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([])
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i,j))

def bfs():
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx,ny))

bfs()

flag = True
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(-1)
            flag = False
            break
    if not flag:
        break

m = 0
if flag:
    for i in range(N):
        m = max(max(graph[i]), m)
    print(m-1)
