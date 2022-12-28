from collections import deque

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[b].append(a)


def bfs(start):
    cnt = 1
    visited[start] = True
    q = deque([start])

    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                q.append(i)
    
    return cnt

answer = []
m = -1
for i in range(1,n+1):
    visited = [False]*(n+1)
    result = bfs(i)

    if result > m:
        answer = [i]
        m = result
    elif result == m:
        answer.append(i)

print(' '.join(map(str,answer)))
