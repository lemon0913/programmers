from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [-1]*(n+1)
def bfs(start):
    visited[start] = 0
    q = deque([start])

    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == -1:
                visited[i] = x
                q.append(i)

bfs(1)

for i in range(2,n+1):
    print(visited[i])
