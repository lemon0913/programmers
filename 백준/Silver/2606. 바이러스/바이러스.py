from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False]*(n+1)
def bfs(start):
    visited[start] = True
    q = deque([start])

    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

bfs(1)
print(visited.count(True)-1)