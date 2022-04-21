from collections import deque
import sys
input = sys.stdin.readline
if __name__ == "__main__":
    N, M, K , X = map(int, input().split())
    graph = [[] for i in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
    
    def bfs(start, c):
        visited[start] = True
        queue = deque()
        queue.append(start)

        while queue:
            v = queue.popleft()
            for x in graph[v]:
                if not visited[x]:
                    queue.append(x)
                    visited[x] = True
                    cnt[x] = cnt[v]+1 # x까지의 거리는 v까지의 거리에 1 더한 것
    
    visited = [False]*(N+1) 
    cnt = [0] * (N+1) # 각 도시까지의 최단거리를 저장하는 리스트
    bfs(X, 0)

    # 각 도시까지의 최단거리가 K와 같으면 그 도시 번호 출력
    # 최단거리가 K인 도시가 하나도 없으면 -1출력
    for i in range(N+1):
        if cnt[i] == K:
            print(i)
    cnt = set(cnt)
    if K not in cnt:
        print(-1)