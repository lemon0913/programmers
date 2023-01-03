from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0]*(n+1)
for i in range(1,n+1):
    parent[i] = i

visited = [False]*(n+1)

def bfs(start):

    visited[start] = True
    q = deque([start])

    while q:
        now = q.popleft()
        for x in graph[now]:
            if not visited[x]:
                visited[x] = True
                parent[x] = now
                q.append(x)

bfs(1)

for i in range(2,n+1):
    print(parent[i])