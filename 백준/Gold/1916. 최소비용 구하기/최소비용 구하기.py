import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

if __name__ == "__main__":
    N = int(input())
    M = int(input())

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b,c))
    start, end = map(int, input().split())
    
    distance = [INF]*(N+1)
    def dijkstra(start):
        distance[start] = 0
        q = []
        heapq.heappush(q, (0,start))

        while q:
            dis, now = heapq.heappop(q)
            if distance[now] < dis:
                continue
            for x in graph[now]:
                cost = dis + x[1]
                if cost < distance[x[0]]:
                    distance[x[0]] = cost
                    heapq.heappush(q, (cost, x[0]))
    
    dijkstra(start)
    print(distance[end])
