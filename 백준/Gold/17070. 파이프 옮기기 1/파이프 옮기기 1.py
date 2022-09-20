# bfs 풀이(시간초과..)
# from collections import deque
# if __name__ == "__main__":
#     N = int(input())
#     graph = []
#     for _ in range(N):
#         graph.append(list(input().split()))

#     visited = [[False]*N for _ in range(N)]
#     def bfs(graph,visited, s,a1,b1,a2,b2):
#         q = deque([(s,a1,b1,a2,b2)])
#         visited[a1][b1] = True
#         visited[a2][b2] = True

#         cnt = 0
#         while q:
#             s, x1, y1, x2, y2 = q.popleft()

#             if x2 == N-1 and y2 == N-1:
#                 cnt += 1
#             else:

#                 # 가로방향으로 놓여있을 때
#                 if s == 1:              
#                     # 1. 오른쪽으로 이동
#                     ny1 = y1 + 2
#                     if 0 <= ny1 < N and graph[x1][ny1] == '0':
#                         if not visited[x1][ny1]:
#                             q.append((1, x2, y2, x1, ny1))
#                     # 2. 대각선으로 회전
#                     nx1 = x1 + 1
#                     if 0 <= nx1 < N and 0 <= ny1 < N and graph[x2+1][y2] == '0' and graph[x2][y2+1] == '0' and graph[x2+1][y2+1] == '0':
#                         if not visited[nx1][ny1]:
#                             q.append((3, x2, y2, nx1, ny1))

#                 # 세로방향으로 놓여있을 때
#                 elif s == 2:
#                     # 1. 아래로 이동
#                     nx1 = x1 + 2
#                     if 0 <= nx1 < N and graph[nx1][y1] == '0':
#                         if not visited[nx1][y1]:
#                             q.append((2, x2, y2, nx1, y1))
#                     # 2. 대각선으로 이동
#                     ny1 = y1 + 1
#                     if 0 <= nx1 < N and 0 <= ny1 < N and graph[x2+1][y2] == '0' and graph[x2][y2+1] == '0' and graph[x2+1][y2+1] == '0':
#                         if not visited[nx1][ny1]:
#                             q.append((3, x2, y2, nx1, ny1))

#                 # 대각선으로 놓여있을 때
#                 else:
#                     # 1. 오른쪽으로 이동
#                     nx1 = x1 + 1
#                     ny1 = y1 + 2
#                     if 0 <= nx1 < N and 0 <= ny1 < N and graph[nx1][ny1] == '0':
#                         if not visited[nx1][ny1]:
#                             q.append((1, x2, y2, nx1, ny1))
#                     # 2. 아래로 이동
#                     nx1 = x1 + 2
#                     ny1 = y1 + 1
#                     if 0 <= nx1 < N and 0 <= ny1 < N and graph[nx1][ny1] == '0':
#                         if not visited[nx1][ny1]:
#                             q.append((2, x2, y2, nx1, ny1))
#                     # 3. 대각선으로 이동
#                     nx1 = x1 + 2
#                     ny1 = y1 + 2
#                     if 0 <= nx1 < N and 0 <= ny1 < N and graph[x2+1][y2] == '0' and graph[x2][y2+1] == '0' and graph[x2+1][y2+1] == '0':
#                         if not visited[nx1][ny1]:
#                             q.append((3, x2, y2, nx1, ny1))

#         return cnt
                
#     print(bfs(graph,visited, 1,0,0,0,1))
                
            
# dp 풀이
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 0: 가로로 온 수 / 1: 세로로 온 수 / 2: 대각선으로 온 수
dp = [[[0] * n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1
i = 2
while i < n:
    if arr[0][i] == 1:
        break
    dp[0][0][i] = 1
    i += 1

for i in range(1, n):
    for j in range(2, n):
        if arr[i][j] == 0 and arr[i][j - 1] == 0 and arr[i - 1][j] == 0:
            dp[2][i][j] = sum(dp[k][i - 1][j - 1] for k in range(3))
        if arr[i][j] == 0:
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

print(sum(dp[i][-1][-1] for i in range(3)))