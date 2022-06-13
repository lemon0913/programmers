import sys
if __name__ == "__main__":
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(list(map(int, sys.stdin.readline().split())))
    
    dp = [0] * (N+1)
    for i in range(N-1, -1, -1):
        # i번째 날을 선택했을 때 날짜를 초과하면
        if lst[i][0] + i > N:
            dp[i] = dp[i+1]
        # i번째 날을 선택했을 때 날짜를 초과하지 않으면
        # i번재 날을 선택했을 때와 dp[i+1]의 값 중에서 큰 값을 선택
        else:
            dp[i] = max(dp[i+1], lst[i][1]+dp[i+lst[i][0]])

    print(dp[0])