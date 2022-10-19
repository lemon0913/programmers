from collections import deque
from copy import deepcopy
from itertools import combinations

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))



walls = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            walls.append((i,j))
walls = list(combinations(walls, 3))


result = -1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for wall in walls:
    c_graph = deepcopy(graph)
    for w in wall:
        c_graph[w[0]][w[1]] = 1
    
    q = deque()
    for i in range(N):
        for j in range(M):
            if c_graph[i][j] == 2:
                q.append((i,j))
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if c_graph[nx][ny] == 0:
                    c_graph[nx][ny] = 2
                    q.append((nx,ny))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if c_graph[i][j] == 0:
                cnt += 1
    
    if cnt > result:
        result = cnt

print(result)