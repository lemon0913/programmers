from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]
rest = []

def bfs(graph, visited):
    q = deque([(0,0)])
    visited[0][0] = True
    cnt = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                else:
                    visited[nx][ny] = True
                    cnt += 1
                    graph[nx][ny] = 0
    
    rest.append(cnt)
    return cnt

time = 0
while True:
    time += 1
    visited = [[False]*m for _ in range(n)]
    cnt = bfs(graph,visited)
    if cnt == 0:
        break

print(time-1)
print(rest[-2])