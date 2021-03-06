if __name__ == "__main__":
    N = int(input())

    dp = [0] * 1000001

    dp[1] = 1
    dp[2] = 2

    # N은 N-1의 경우들에 '1'을 붙여 만들거나 N-2의 경우들에 '00'을 붙여서 만들 수 있음
    # 따라서 dp[i] = dp[i-1] + dp[i-2]
    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2])%15746
    
    print(dp[N])