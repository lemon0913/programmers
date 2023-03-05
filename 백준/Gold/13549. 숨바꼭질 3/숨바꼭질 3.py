from collections import deque

n, k = map(int, input().split())

visited = [-1]*(100001)

dx = [-1,1]
def bfs(s,e):
    visited[s] = 0
    q = deque([s])

    while q:
        x = q.popleft()
        # 종료조건
        if x == e:
            return visited[x]
        
        # 1) 순간이동을 하는 경우
        nx = 2*x
        if 0 <= nx <= 100000 and visited[nx] == -1:
            visited[nx] = visited[x]
            q.appendleft(nx)
        # 2) 걷는 경우
        for i in range(2):
            nx = x + dx[i]
            if 0 <= nx <= 100000 and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                q.append(nx)


print(bfs(n,k))
