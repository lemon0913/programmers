# 10점짜리 풀이...런타임 에러 엄청나게 뜸...
# 생각해보니 쓸데없이 복잡하게 품
# INF = int(1e9)
# def solution(m, n, puddles):
    
    
#     graph = []
#     for i in range(n):
#         if i == 0:
#             graph.append([1]*m)
#         else:
#             graph.append([1]+[0]*(m-1))

    
#     for i in range(len(puddles)):
#         x, y = puddles[i][0]-1, puddles[i][1]-1
#         graph[x][y] = INF
    

#     for j in range(1, n):
#         for i in range(1, m):
#             if graph[j][i] == INF:
#                 pass
#             else:
#                 if graph[j-1][i] != INF:
#                     graph[j][i] += graph[j-1][i]
#                 if graph[j][i-1] != INF:
#                     graph[j][i] += graph[j][i-1]
    
                    
#     return graph[n-1][m-1]%1000000007



# 타인 참고 풀이
def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles]      # 미리 puddles 좌표 거꾸로
    dp = [[0] * (m + 1) for i in range(n + 1)]  # dp 초기화
    dp[1][1] = 1           # 집의 위치(시작위치)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: continue 
            if [i, j] in puddles:    # 웅덩이 위치의 경우 값을 0으로
                dp[i][j] = 0
            else:                    # 현재 칸은 왼쪽 칸, 위 칸의 합산!
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    return dp[n][m]


