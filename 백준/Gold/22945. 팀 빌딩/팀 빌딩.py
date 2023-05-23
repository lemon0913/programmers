# 구간이 좁아질수록 사이에 있는 개발자 수는 감소하나 능력치의 최소값은 증가할 수 있따
# 따라서 구간을 좁혀가며 연산

n  = int(input())
power = list(map(int, input().split()))

maxV = 0
l = 0
r = n-1
while l+1 < r:
    maxV = max(maxV, (r-l-1)*min(power[l],power[r]))

    # 포인터를 이동할 때 더 작은 값을 가리키고 있는 포인터를 이동시키자
    if power[l] < power[r]:
        l += 1
    else:
        r -= 1

print(maxV)