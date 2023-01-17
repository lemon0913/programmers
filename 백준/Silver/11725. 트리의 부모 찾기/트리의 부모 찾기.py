# 이렇게 하는거 전혀 아님...이건 단순 부모가 아닌 루트를 찾는거네..

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent,parent[x])
#     return parent[x]

# def union_parent(parent,a,b):
#     a = find_parent(parent,a)
#     b = find_parent(parent,b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# n = int(input())
# parent = [0]*(n+1)
# for i in range(1,n+1):
#     parent[i] = i

# for _ in range(n-1):
#     a,b = map(int, input().split())
#     if find_parent(parent,a) != find_parent(parent,b):
#         union_parent(parent,a,b)

# print(parent)

################################################

# 그냥 bfs로 풀면 되는거란다...

from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0]*(n+1)
visited = [False]*(n+1)

def bfs(start,visited,parent):
    visited[start] = True
    q = deque([start])

    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                parent[next] = now
                q.append(next)

bfs(1,visited,parent)

for i in range(2,n+1):
    print(parent[i])
