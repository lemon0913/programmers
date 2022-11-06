from collections import deque

N, M = map(int, input().split())

visited = [[[-1]*2 for _ in range(M)] for _ in range(N)]

graph = []
for _ in range(N):
    graph.append(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(a,b,flag):
    visited[a][b][flag] = 1
    q = deque([(a,b,flag)])

    
    while q:
        x,y,flag = q.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][flag]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                # 현재 위치가 벽이고 벽을 뚫을 기회도 있다
                if graph[nx][ny] == '1' and flag == 0:
                    # if visited[nx][ny] == -1:
                        visited[nx][ny][1] = visited[x][y][0]+1
                        q.append((nx,ny,1))
                
                # 현재 위치가 벽이 아니라면 그냥 갈 수 있음
                if graph[nx][ny] == '0':
                    if visited[nx][ny][flag] == -1:
                        visited[nx][ny][flag] = visited[x][y][flag]+1
                        q.append((nx,ny,flag))
    
    return -1
    


print(bfs(0,0,0))