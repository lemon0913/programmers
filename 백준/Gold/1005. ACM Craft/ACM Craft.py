from collections import deque

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        times = [0] + list(map(int, input().split()))
        indegree = [0]*(N+1)
        graph = [[] for _ in range(N+1)]
        for _ in range(K):
            X, Y = map(int, input().split())
            graph[X].append(Y)
            indegree[Y] += 1
        
        W = int(input())

        def topology(W):
            dp = [0]*(N+1)
            q = deque()

            # 진입차수가 0인 노드를 큐에 삽입
            for i in range(1, N+1):
                if indegree[i] == 0:
                    q.append(i)
                    dp[i] = times[i]
            
            while q:
                now = q.popleft()
                for x in graph[now]:
                    # 해당 노드와 연결된 노드들의 진입차수 1 빼기
                    indegree[x] -= 1
                    dp[x] = max(dp[x], dp[now]+times[x]) # 이게 중요한 부분!!! 여기서 dp 활용!!
                    if indegree[x] == 0:
                        q.append(x)
                
                if now == W:
                    return dp[W]
        
        print(topology(W))
                