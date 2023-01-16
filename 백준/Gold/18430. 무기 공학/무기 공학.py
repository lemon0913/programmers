
n, m = map(int, input().split())
tree = []
for _ in range(n):
    tree.append(list(map(int, input().split())))

result = 0
visited = [[False]*m for _ in range(n)]
shape = [[0,-1,1,0],[-1,0,0,-1],[-1,0,0,1],[0,1,1,0]]

def dfs(a,b,visited,r):
    global result
    if b == m:
        a += 1
        b = 0
    if a == n:
        result = max(result,r)
        return
    
    if not visited[a][b]:
        for k in range(4):
            x,y,xx,yy = a+shape[k][0], b+shape[k][1], a+shape[k][2], b+shape[k][3]
            if 0 <= x < n and 0 <= y < m and 0 <= xx < n and 0 <= yy < m and not visited[x][y] and not visited[xx][yy]:
                visited[a][b] = visited[x][y] = visited[xx][yy] = True
                dfs(a,b+1,visited,r+tree[a][b]*2+tree[x][y]+tree[xx][yy])
                visited[a][b] = visited[x][y] = visited[xx][yy] = False
    
    dfs(a,b+1,visited,r)

dfs(0,0,visited,0)

print(result)
