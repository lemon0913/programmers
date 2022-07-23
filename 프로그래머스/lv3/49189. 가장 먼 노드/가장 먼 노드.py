import heapq
INF = int(1e9)

def solution(n, edge):
    
    
    graph = [[] for _ in range(n+1)]
    for i in range(len(edge)):
        a, b = edge[i][0], edge[i][1]
        graph[a].append((b,1))
        graph[b].append((a,1))
    
    distance = [INF] * (n+1)
    
    def dijkstra(start):
        distance[start] = 0
        h = []
        heapq.heappush(h, (0, start))
        
        while h:
            dist, now = heapq.heappop(h)
            if dist > distance[now]:
                continue
            for x in graph[now]:
                cost = dist + x[1]
                if cost < distance[x[0]]:
                    distance[x[0]] = cost
                    heapq.heappush(h, (cost, x[0]))
    
    dijkstra(1)
    
    # 최대 거리 구하기
    m = 0
    for d in distance:
        if d != INF and d > m:
            m = d
    
    # 가장 멀리 떨어진 노드 구하기
    answer = 0
    for d in distance:
        if d == m:
            answer += 1
    
    return answer