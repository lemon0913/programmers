# 이거 진짜 3번째 푸는거 같은데 여전히 이해 안됨....ㅋㅋㅋㅋㅋ쿠ㅠㅜㅠㅜㅠ
if __name__ == "__main__":
    N = int(input())
    dp = [0]*(N+1)
    T, P = [], []
    for _ in range(N):
        t, p = map(int, input().split())
        T.append(t)
        P.append(p)
    
    M = 0
    for i in range(N):
        M = max(M, dp[i])
        if i + T[i] <= N:
            dp[i+T[i]] = max(M+P[i], dp[i+T[i]])
            
    print(max(dp))