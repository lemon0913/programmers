from itertools import combinations
INF = int(1e9)

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


arr = []
for i in range(1, N-1):
    for j in range(1, N-1):
        arr.append((i,j))

arr = list(combinations(arr, 3))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def minimun(a, graph):
    result = 0
    visited = [[False]*N for _ in range(N)]
    for i in range(3):
        x, y = a[i][0], a[i][1]
        if visited[x][y]:
            return INF
        visited[x][y] = True
        result += graph[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if visited[nx][ny]:
                return INF
            visited[nx][ny] = True
            result += graph[nx][ny]
    
    return result

m = INF

for a in arr:
    result = minimun(a, graph)
    if result < m:
        m = result

print(m)