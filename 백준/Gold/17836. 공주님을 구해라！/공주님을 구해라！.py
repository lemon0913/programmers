from collections import deque

INF = int(1e9)


N, M, T = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))



dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


# 1. 그람을 찾지 않고 최단거리로
visited = [[0]*M for _ in range(N)]
def bfs1(visited, graph, a,b):
    visited[a][b] = 1
    q = deque([(a,b)])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and graph[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
            
            
bfs1(visited,graph,0,0)
result1 = visited[N-1][M-1]-1
if result1 == -1:
    result1 = INF


# 2.그람을 찾고 난 뒤 최단거리로
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            gx = i
            gy = j

visited = [[0]*M for _ in range(N)]
def bfs2(visited, graph, a,b):

    visited[a][b] = 1
    q = deque([(a,b)])

    while q:
        x,y = q.popleft()
        if x == gx and y == gy:
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and graph[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))

bfs2(visited,graph,0,0)
result2 = visited[gx][gy]-1
if result2 != -1:
    result2 += (N-1-gx + M-1-gy)
else:
    result2 = INF



result = min(result1, result2)
if result > T:
    print('Fail')
else:
    print(result)