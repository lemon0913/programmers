from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

visited = [[False]*M for i in range(N)]
def bfs(a, b):
    visited[a][b] = True
    queue = deque()
    queue.append((a,b))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0 <= ny < M:
                if visited[nx][ny] == False and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
    

bfs(0, 0)
print(graph[N-1][M-1])