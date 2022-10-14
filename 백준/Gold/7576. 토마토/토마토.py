from collections import deque


M, N = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i,j))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx,ny))


flag = True
m = -1
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            flag = False
            break
        elif graph[i][j] > m:
            m = graph[i][j]
    if not flag:
        break

if not flag:
    print(-1)
else:
    print(m-1)



# from collections import deque


# M, N = map(int, input().split())
# graph = []
# for _ in range(N):
#     graph.append(list(map(int, input().split())))


# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs(graph, a, b):
#     q = deque([(a,b)])

#     while q:
#         x,y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < N and 0 <= ny < M:
#                 if graph[nx][ny] == 0 or graph[nx][ny] > graph[x][y] + 1:
#                     graph[nx][ny] = graph[x][y] + 1
#                     q.append((nx,ny))

# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == 1:
#             bfs(graph,i,j)

# flag = True
# m = -1
# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == 0:
#             flag = False
#             break
#         elif graph[i][j] > m:
#             m = graph[i][j]
#     if not flag:
#         break

# if not flag:
#     print(-1)
# else:
#     print(m-1)