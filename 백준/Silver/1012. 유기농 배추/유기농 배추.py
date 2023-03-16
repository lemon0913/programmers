from collections import deque

t = int(input())
for _ in range(t):
    m,n,k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        a,b = map(int, input().split())
        graph[b][a] = 1
    
    visited = [[False]*m for _ in range(n)]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    cnt = 0
    def bfs(a,b):
        global cnt
        visited[a][b] = True
        q = deque([(a,b)])

        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx,ny))
        
        cnt += 1
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
    
    print(cnt)