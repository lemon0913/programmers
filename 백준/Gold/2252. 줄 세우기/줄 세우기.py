from collections import deque

if __name__ == "__main__":
    N, M = map(int, input().split())
    indegree = [0]*(N+1)
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
        indegree[B] += 1
    
    def topology():
        q = deque()
        result = []

        for i in range(1, N+1):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            now = q.popleft()
            result.append(now)

            for x in graph[now]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    q.append(x)
        
        for i in result:
            print(i, end = ' ')
    
    topology()