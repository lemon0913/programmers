import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문할 수 있는 점이 여러개인 경우 정점 번호가 작은 것을 먼저 방문
for i in range(N+1):
    graph[i].sort()

def dfs(start):
    visited[start] = True
    print(start, end = ' ')

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    print(start, end = ' ')
    visited[start] = True
    queue = deque()
    queue.append(start)

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                print(i, end=' ')
                visited[i] = True
                queue.append(i)


visited = [False]*(N+1)
dfs(V)
print()

visited = [False]*(N+1)
bfs(V)
