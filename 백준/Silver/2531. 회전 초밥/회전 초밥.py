# k를 연속 먹으면 할인 가격 
# k를 연속 먹으면 쿠폰에 적혀진 종류의 초밥을 무료로 제공
# 가능한 다양한 종류의 초밥을 먹자

# k개 연속하며, 다 다른 종류 & 쿠폰은 또 연속한 것과 다른 것

import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
susi = []
for _ in range(n):
    susi.append(int(input()))


answer = 0
end = 0
tmp = []
for start in range(n):
    while end < n+k and end - start < k:
        if end >= n:
            eend  = end - n
        else:
            eend = end
        tmp.append(susi[eend])
        end += 1
    
    if end - start == k:
        l = len(set(tmp))
        if c not in tmp:
            l += 1
        answer = max(answer,l)
    
    tmp.pop(0)

print(answer)