import heapq
INF = int(1e9)

if __name__ == "__main__":
    N, K = map(int, input().split())
    visited = [INF]*100001

    # 다익스트라 알고리즘 수행
    q = []
    visited[N] = 0
    heapq.heappush(q, (0, N))
    while q:
        dist, now = heapq.heappop(q)
        if visited[now] < dist:
            continue
        
        if 0 <= now+1 <= 100000:
            cost = dist + 1
            if cost < visited[now+1]:
                visited[now+1] = cost
                heapq.heappush(q, (cost, now+1))

        if 0 <= now-1 <= 100000:
            cost = dist + 1
            if cost < visited[now-1]:
                visited[now-1] = cost
                heapq.heappush(q, (cost, now-1))

        if 0 <= now*2 <= 100000:
            cost = dist
            if cost < visited[now*2]:
                visited[now*2] = cost
                heapq.heappush(q, (cost, now*2))

    print(visited[K])