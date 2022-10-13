from collections import deque
INF = int(1e9)

N, K = map(int, input().split())

visited = [-1]*100001

def bfs(start):

    visited[start] = 0
    q = deque([start])    

    while q:

        x = q.popleft()
      
        y = x*2
        if 0 <= y <= 100000:
            if visited[y] == -1:
                visited[y] = visited[x]
                q.appendleft(y)

        for y in [x+1, x-1]:
            if 0 <= y <= 100000:
                if visited[y] == -1:
                    visited[y] = visited[x]+1
                    q.append(y)

bfs(N)

print(visited[K])