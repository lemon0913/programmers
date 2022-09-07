from collections import deque
if __name__ == "__main__":
    N, M, K = map(int, input().split())

    graph = [[0]*M for _ in range(N)]
    for _ in range(K):
        r, c = map(int, input().split())
        graph[r-1][c-1] = 1
    
    visited = [[False]*M for _ in range(N)]


    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    def bfs(a, b, visited, graph):
        q = deque([(a,b)])
        visited[a][b] = True

        cnt = 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if not visited[nx][ny] and graph[nx][ny] == 1:
                        visited[nx][ny] = True
                        q.append((nx,ny))
                        cnt += 1
        
        return cnt
    
    result = []
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] == 1:
                result.append(bfs(i, j, visited, graph))
    
    print(max(result))