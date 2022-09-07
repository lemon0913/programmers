from collections import deque
if __name__ == "__main__":
    A, B = map(int, input().split())

    
    def bfs(start, end):
        q = deque([(start, 1)])
        

        while q:
            v, cnt = q.popleft()
            t1 = 2*v
            t2 = int(str(v)+'1')

            if t1 == end or t2 == end:
                return cnt+1
            else:
                if t2 < end :
                    q.append((t2, cnt+1))
                if t1 < end :
                    q.append((t1, cnt+1))
            
        
        return -1
    
    print(bfs(A, B))