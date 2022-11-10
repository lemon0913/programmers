
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


result = []
visited = [[False]*M for _ in range(N)]
shape = {0:[0,-1,1,0], 1:[-1,0,0,-1], 2:[-1,0,0,1], 3:[0,1,1,0]}
def dfs(i,j,s):
    # 종료 조건을 못 잡음...
    if j == M:
        i += 1
        j = 0
    if i == N:
        result.append(s)
        return
    
    if not visited[i][j]:
        for k in range(4):
            a,b,c,d = shape[k]
            x,y,xx,yy = i+a, j+b, i+c, j+d
            if 0 <= x < N and 0 <= y < M and 0 <= xx < N and 0 <= yy < M:
                if not visited[x][y] and not visited[xx][yy]:
                    visited[i][j] = visited[x][y] = visited[xx][yy] = True
                    dfs(i,j+1,s+graph[i][j]*2+graph[x][y]+graph[xx][yy])
                    visited[i][j] = visited[x][y] = visited[xx][yy] = False
    dfs(i,j+1,s)

dfs(0,0,0)
print(max(result))