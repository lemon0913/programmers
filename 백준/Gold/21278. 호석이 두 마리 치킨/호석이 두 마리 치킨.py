# n개의 건물과 m개의 도로로 이어져있으며, 도로는 양방향
# 2개의 건물을 골라 치킨집을 열 때, 모든 건물에서 접근성의 합을 최소화
# 접근성? 건물에서 치킨집까지 왕복 최단시간


# 치킨집을 차릴 2개의 건물을 선택 -> 조합
# 각 경우마다 다른 건물에서 치킨집까지의 접근성의 합을 구하기
# 접근 시간의 합이 같은 경우, 번호가 더 작은 걸 출력


# from itertools import combinations
# from collections import deque
# import sys

# # 한 건물에서 다른 건물까지 거리를 구하는 함수
# def bfs(start,end):
#     q = deque([start])
#     visited[start] = 0
#     cnt = 0

#     while q:
#         now = q.popleft()
#         if now == end:
#             return visited[end]
#         for x in graph[now]:
#             if visited[x] == -1:
#                 visited[x] = visited[now]+1
#                 q.append(x)

# n,m = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     a,b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
# result = []

# # 건물 2개를 고르는 경우의 수 구하기
# chicken = list(combinations(list(range(1,n+1)),2))


# # 각 경우의 수 마다 전급성의 합 구하기
# for ch in chicken:
#     cost = 0
#     for start in range(1,n+1):
#         if start not in ch:
#             tmp = sys.maxsize
#             for end in ch:
#                 visited = [-1]*(n+1)
#                 tmp = min(tmp, bfs(start,end)*2)
#             cost += tmp
#     result.append((ch[0],ch[1],cost))

# # 접근 시간이 가장 작고, 건물 번호도 가장 작은 경우 출력   
# result.sort(key = lambda x:(x[2],x[0],x[1]))
# print(result[0][0], result[0][1], result[0][2])

##################################################################3
# 시간 초과
# 어차피 모든 건물 간의 이동 경로를 구하는 것이니 플로이드 워셜 알고리즘 사용

from itertools import combinations
import sys
INF = int(1e9)
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1,n+1):
    graph[i][i] = 0

# 플로이드 워셜 알고리즘으로 한 건물에서 다른 건물까지 가는데 걸리는 시간 전부 구하기
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 치킨집을 차릴 2개의 건물을 선택하는 모든 경우의 수 구하기
chicken = list(combinations(list(range(1,n+1)),2))

# 각 경우의 수 마다 접근성의 합 구하기
result = []
for ch in chicken:
    cost = 0
    for start in range(1,n+1):
        tmp = INF
        for end in ch:
            tmp = min(tmp, graph[start][end]*2)
        cost += tmp
    result.append((ch[0],ch[1],cost))


# 접근 시간이 가장 작고, 건물 번호도 가장 작은 경우 출력   
result.sort(key = lambda x:(x[2],x[0],x[1]))
print(result[0][0], result[0][1], result[0][2])
