import sys

n = int(input())
water = list(map(int, input().split()))

start = 0
end = n-1
answer = sys.maxsize
while start < end:
    tmp = water[start] + water[end]

    if tmp > 0:
        end -= 1
    
    elif tmp < 0:
        start += 1
    else:
        answer = tmp
        break
    
    if abs(answer) > abs(tmp):
        answer = tmp

print(answer)
