# bfs 풀이인데 메모리초과 남...
# if __name__ == '__main__':
#     n, k = map(int, input().split())
#     coin = []
#     for _ in range(n):
#         coin.append(int(input()))
    
#     coin.sort(reverse = True)
    
#     answer = 0
#     def bfs(k, answer):
#         arr = [[] for _ in range(n)]
#         arr[0].append(k)

#         for j in range(n):
#             while arr[j]:
#                 r = arr[j].pop()
#                 if j != n-1:
#                     for i in range(k):
#                         result = r - coin[j] * i
#                         if result > 0:
#                             arr[j+1].append(result)
#                         elif result == 0:
#                             answer += 1
#                             break
#                         else:
#                             break
#                 else:
#                     if r % coin[j] == 0:
#                         answer += 1
        
#         return answer
            
#     print(bfs(k, answer))
    

    
# dp로 풀어야함
# 왜 dp? 해당 차수의 경우의 수를 구할 때 앞에서 구했던 경우의 수를 이용하기 때문에!
# https://velog.io/@ready2start/Python-%EB%B0%B1%EC%A4%80-2293-%EB%8F%99%EC%A0%84-1
#    1   2   3   4   5   6   7   8   9   10
# 5  0   0   0   0   1   0   0   0   0   1
# 2  0   1   0   1   0   1   1   1   1   1
# 1  1   1   2   2   3   4   5   6   7   8

if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = []
    for _ in range(n):
        coins.append(int(input()))
    
    dp = [0] * (k+1)
    dp[0] = 1 # 동전 1개 쓰는 경우를 위해!

    for coin in coins:
        for i in range(1, k+1):
            if i - coin >= 0:
                dp[i] += dp[i-coin]
    print(dp[k])