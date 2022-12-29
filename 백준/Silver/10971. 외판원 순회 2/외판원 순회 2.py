
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


m = int(1e9)
def dfs(graph,visited,a,s):
    global m, result

    if len(a) == n:
        if graph[a[-1]][a[0]] != 0:
            s += graph[a[-1]][a[0]]
            m = min(s,m)
        return
    
    for i in range(n):
        if not visited[i] and graph[a[-1]][i] != 0:
            tmp = s
            visited[i] = True 
            s += graph[a[-1]][i]
            a.append(i)
            dfs(graph,visited,a,s)
            visited[i] = False
            s = tmp
            a.pop()

for i in range(n):
    visited = [False]*(n+1)
    visited[i] = True
    dfs(graph,visited,[i],0)

print(m)