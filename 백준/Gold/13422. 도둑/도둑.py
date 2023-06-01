# 붙잡히지 않고 도둑질 할 경우의 수
# 예외케이스가 하나 있음.. 
# 4 4 5
# 1 1 1 1
# 이 경우 정담은 1인데 그냥 풀면 4가 나옴, n과 m이 같을 떄 예외처리를 해야 함

import sys
input = sys.stdin.readline

def solution(houses, N, M, K):
    currentSum = sum(houses[0:M])
    left = 1
    right = M
    answer = 1 if currentSum < K else 0
    # 예외처리
    if N == M:
        return answer

    while left < N:
        currentSum -= houses[left - 1]
        currentSum += houses[right % N]
        if currentSum < K:
            answer += 1
        left += 1
        right += 1
    return answer

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    houses = list(map(int, input().split()))
    print(solution(houses, N, M, K))