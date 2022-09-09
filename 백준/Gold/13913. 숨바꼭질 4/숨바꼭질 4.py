from collections import deque
if __name__ == "__main__":
    N, K = map(int, input().split())

    def path(x, cnt):
        arr = [x]
        tmp = x
        for _ in range(cnt):
           arr.append(before[tmp])
           tmp = before[tmp] 
        
        arr.reverse()
        print(' '.join(map(str, arr)))
        
    
    visited = [-1]*100001
    before = [-1]*100001
    
    visited[N] = 0
    q = deque([N])

    while q:
        x = q.popleft()
        if x == K:
            print(visited[x])
            path(x, visited[x])
            break
        else:
            for nx in (x+1, x-1, 2*x):
                if 0 <= nx <= 100000 and visited[nx] == -1:
                    visited[nx] = visited[x]+1
                    before[nx] = x
                    q.append(nx)
        