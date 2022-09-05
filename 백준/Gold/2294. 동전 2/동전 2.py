# 얘도 dp로 풀어야함
# 동전 1처럼 dp 표를 그려보면 알 수 있다
# 단 이번에는 동전 단위가 큰 경우부터 표 채우기
#     1   2   3   4   5   6   7   8   9   10   11   12   13   14   15
# 12  x   x   x   x   x   x   x   x   x   x    x    1    x    x    x
# 5   x   x   x   x   1   x   x   x   x   2    x    1    x    x    3   
# 1   1   2   3   4   1   2   3   4   5   2    3    1    2    3    4

INF = int(1e9)
if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = []
    for _ in range(n):
        coins.append(int(input()))
    coins.sort(reverse=True)
    coins = [0] + coins
    
    dp = [[INF]*(k+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    
    for j in range(1, n+1):
        for i in range(coins[j], k+1):
            dp[j][i] = min(dp[j-1][i], dp[j][i-coins[j]]+1)
    
    if dp[n][k] == INF:
        print(-1)
    else:
        print(dp[n][k])