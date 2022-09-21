if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        dp = [1] * 10001

        for i in range(2, n+1):
            dp[i] += dp[i-2] 
        
        for i in range(3, n+1):
            dp[i] += dp[i-3]
        
        print(dp[n])