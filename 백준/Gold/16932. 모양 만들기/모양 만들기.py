# from collections import deque

# N, M = map(int, input().split())

# graph = []
# for i in range(N):
#     graph.append(list(map(int, input().split())))

# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# def bfs(visited, graph, a,b):
#     visited[a][b] = True
#     q = deque([(a,b)])

#     cnt = 1
#     while q:
#         x,y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if not visited[nx][ny] and graph[nx][ny] == 1:
#                     cnt += 1
#                     visited[nx][ny] = True
#                     q.append((nx,ny))
    
#     return cnt

# result = []
# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == 0:
#             visited = [[False]*M for _ in range(N)]
#             graph[i][j] = 1
            
#             m = 0
#             for a in range(N):
#                 for b in range(M):
#                     if graph[a][b] == 1 and not visited[a][b]:
#                         m = max(m,bfs(visited,graph,a,b))
            
#             result.append(m)
#             graph[i][j] = 0

# print(max(result))

###############################################3

# ...시간초과 남...
# 배열의 1을 그룹핑해주는 것이 이 문제의 해결법
from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

visited = [[0]*M for _ in range(N)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs(visited, graph, a,b):
    visited[a][b] = num
    q = deque([(a,b)])

    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    cnt += 1
                    visited[nx][ny] = num
                    q.append((nx,ny))
    
    return cnt

# '1' 그룹화 진행
num = 1
group = {}
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt = bfs(visited,graph,i,j)
            group[num] = cnt
            num += 1

# 배열을 순차적으로 돌면서 배열에 인접한 1을 만나면 그 1이 어떤 그룹인지 확인하고 set에 넣는다
# 만약 중복된다면 넣어주지 않는다
result = 0
for a in range(N):
    for b in range(M):
        if graph[a][b] == 0:
            s = set()
            for i in range(4):
                na = a + dx[i]
                nb = b + dy[i]
                if 0 <= na < N and 0 <= nb < M:
                    if graph[na][nb] == 1 and visited[na][nb] not in s:
                        s.add(visited[na][nb])
            
            res = 1
            for ss in s:
                res += group[ss]
            result = max(result, res)

print(result)