

# .은 빈 필드, #은 울타리, o는 양, v는 늑대
# 울타리에 막혀 있지 않으면 같은 영역

from collections import deque

r,c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(input())

save_sheep = 0
save_wolf = 0

visited = [[False]*c for _ in range(r)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]


def bfs(a,b):
    global save_sheep, save_wolf

    visited[a][b] = True
    q = deque([(a,b)])

    sheep = 0
    wolf = 0
    while q:
        x,y = q.popleft()
        
        if graph[x][y] == 'o':
            sheep += 1
        elif graph[x][y] == 'v':
            wolf += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != '#':
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))
    
    if sheep > wolf:
        save_sheep += sheep
    else:
        save_wolf += wolf

for i in range(r):
    for j in range(c):
        if graph[i][j] != '#' and not visited[i][j]:
            bfs(i,j)

print(save_sheep, save_wolf)