

# 1.모든 요청을 만족 가능 -> 요청한 금액 그대로 배정
# 2.모든 요청을 만족 불가 -> 정수 상한액 계산 
#   -> 상한액보다 큰 요청은 그냥 상한액을 배정, 상한액보다 작은 요청은 요청 금액 배정
# 2-2.이분탐색을 통해 최대의 정수 상한액을 구하기

n = int(input())
ask = list(map(int, input().split()))
m = int(input())


# 1.모든 요청을 만족할 수 있으면 요청 금액 그대로 배정
if sum(ask) <= m:
    print(max(ask))
# 2.모든 요청을 만족할 수 없으면 최대 정수 상한액을 이분탐색으로 구하기
else:
    start = 0
    end = max(ask)
    result = 0
    while start <= end:
        mid = (start+end)//2

        # 상한액에 따른 총액 구하기
        cost = 0
        for a in ask:
            if a >= mid:
                cost += mid
            else:
                cost += a
        
        # 총액에 따른 이분탐색
        if cost == m:
            result = mid
            break
        elif cost > m:
            end = mid-1
        else:
            result = mid
            start = mid+1

    print(result)