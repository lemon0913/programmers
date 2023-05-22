from collections import deque

t = int(input())
for _ in range(t):
    l = int(input())
    x1,y1 = map(int, input().split())
    x2,y2 = map(int, input().split())

    visited = [[-1]*l for _ in range(l)]
    da = [1,2,-1,-2,1,2,-1,-2]
    db = [2,1,2,1,-2,-1,-2,-1]

    visited[x1][y1] = 0
    q = deque([(x1,y1)])
    while q:
        a,b = q.popleft()
        if a == x2 and b == y2:
            print(visited[a][b])
            break
        for i in range(8):
            na = a + da[i]
            nb = b + db[i]
            if 0 <= na < l and 0 <= nb < l:
                if visited[na][nb] == -1:
                    visited[na][nb] = visited[a][b]+1
                    q.append((na,nb))