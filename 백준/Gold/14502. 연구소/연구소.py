from collections import deque
from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


result = []
def bfs(t_graph):
    q = deque([])
    for i in range(N):
        for j in range(M):
            if t_graph[i][j] == 2:
                q.append((i,j))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if t_graph[nx][ny] == 0:
                    t_graph[nx][ny] = 2
                    q.append((nx,ny))
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if t_graph[i][j] == 0:
                cnt += 1
    result.append(cnt)

c = []
for a in range(N):
    for b in range(M):
        c.append((a,b))

# 벽을 세울 위치 3군데를 조합으로 구하기
com = list(combinations(c, 3))

for x,y,z in com:
    t_graph = deepcopy(graph)
    if t_graph[x[0]][x[1]] == 0 and t_graph[y[0]][y[1]] == 0 and t_graph[z[0]][z[1]] == 0:
        t_graph[x[0]][x[1]] = 1
        t_graph[y[0]][y[1]] = 1
        t_graph[z[0]][z[1]] = 1
        bfs(t_graph)


print(max(result))