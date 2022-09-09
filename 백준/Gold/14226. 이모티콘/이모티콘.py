from collections import deque
if __name__ == "__main__":
    S = int(input())

    # visited = [-1]*1001
    # visited[1] = 0

    q = deque([(1, -1, 0)])
    s = set()
    while q:
        x, tmp, cnt = q.popleft()
        if x == S:
            print(cnt)
            break
        
        # 1개 뺴기
        if x >= 1 and (x-1, tmp) not in s:
            q.append((x-1, tmp, cnt+1))
            s.add((x-1, tmp))
        # 붙여넣기
        if tmp != -1 and (x+tmp, tmp) not in s:
            q.append((x+tmp, tmp, cnt+1))
            s.add((x+tmp, tmp))
        # 복사하기
        if (x,x) not in s:
            q.append((x,x,cnt+1))
            s.add((x,x))