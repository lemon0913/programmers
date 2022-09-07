from collections import deque
if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = []
    for _ in range(M):
        graph.append(input())
    
    visited = [[False]*N for _ in range(M)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    def bfs_W(a, b, visited, graph):
        visited[a][b] = True
        q = deque([(a,b)])

        cnt = 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < M and 0 <= ny < N:
                    if not visited[nx][ny] and graph[nx][ny] == 'W':
                        visited[nx][ny] = True
                        cnt += 1
                        q.append((nx,ny))
        
        return cnt*cnt

    def bfs_B(a, b, visited, graph):
        visited[a][b] = True
        q = deque([(a,b)])

        cnt = 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < M and 0 <= ny < N:
                    if not visited[nx][ny] and graph[nx][ny] == 'B':
                        visited[nx][ny] = True
                        cnt += 1
                        q.append((nx,ny))
        
        return cnt*cnt
    
    cnt_W = 0
    cnt_B = 0
    for i in range(M):
        for j in range(N):
            if not visited[i][j]:
                if graph[i][j] == 'W':
                    cnt_W += bfs_W(i, j, visited, graph)
                else:
                    cnt_B += bfs_B(i, j, visited, graph)
    
    print(cnt_W, cnt_B)