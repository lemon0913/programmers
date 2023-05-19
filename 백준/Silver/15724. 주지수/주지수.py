import sys
input = sys.stdin.readline

n,m = map(int, input().split())
town = []
for _ in range(n):
    town.append(list(map(int, input().split())))

dp = [[0]*m for _ in range(n)]
dp[0][0] = town[0][0]
for i in range(n):
    for j in range(m):
        if i == 0 and j != 0:
            dp[i][j] = dp[i][j-1] + town[i][j]
        
        elif j == 0 and i != 0:
            dp[i][j] = dp[i-1][j] + town[i][j]
        
        elif i != 0 and j != 0:
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + town[i][j]

    
k = int(input())
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    if x1 == 0 and y1 == 0:
        print(dp[x2][y2])

    elif x1 == 0 and y1 != 0:
        print(dp[x2][y2] - dp[x2][y1-1])
    
    elif x1 != 0 and y1 == 0:
        print(dp[x2][y2] - dp[x1-1][y2])
    else:
        print(dp[x2][y2]+dp[x1-1][y1-1]-dp[x2][y1-1]-dp[x1-1][y2])    
