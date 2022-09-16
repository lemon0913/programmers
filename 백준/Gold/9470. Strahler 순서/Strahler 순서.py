from collections import deque
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        K, M, P = map(int, input().split())
        graph = [[] for _ in range(M+1)]
        for i in range(P):
            A, B = map(int, input().split())
            graph[B].append(A)

        visited = [0] * (M+1)
        t = set()
        q = deque([])
        for i in range(1, M+1):
            if len(graph[i]) == 0:
                visited[i] = 1
                t.add(i)
            else:
                q.append(i)
        
        
        while q:
            
            v = q.popleft()
            if set(graph[v])|t != t:
                q.append(v)
                continue
            else:
                t.add(v)
                c = 0
                m = 0
                for x in graph[v]:
                    if visited[x] > m:
                        m = visited[x]
                        c = 1
                    elif visited[x] == m:
                        c += 1
                
                if c == 1:
                    visited[v] = m
                else:
                    visited[v] = m+1
        
        print(K, max(visited))