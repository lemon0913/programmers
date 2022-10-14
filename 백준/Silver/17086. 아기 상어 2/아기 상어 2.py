from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
def bfs(a,b,visited,graph):
    visited[a][b] = 0
    q = deque([(a,b)])

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                if graph[nx][ny] == 1:
                    return visited[nx][ny]
                q.append((nx,ny))

result = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            visited = [[-1]*M for _ in range(N)]
            result.append(bfs(i,j,visited,graph))

print(max(result))
                