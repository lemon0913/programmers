from collections import deque
if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    
    dx = [-1, 1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, 1, -1, -1, 1]
    
    def bfs(visited,a,b):
        q = deque([(a,b)])
        visited[a][b] = 0
        
        while q:
            x, y = q.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < M:
                    if graph[nx][ny] == 1:
                        return visited[x][y] + 1
                    elif graph[nx][ny] == 0 and visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y]+1
                        q.append((nx,ny))
    
    
    result = []
    for i in range(N):
        for j in range(M):
            visited = [[-1]*M for _ in range(N)]
            if graph[i][j] == 0:
                result.append(bfs(visited, i,j))
    
    print(max(result))