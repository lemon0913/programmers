
# 이분탐색 기본

n = int(input())

start = 0
end = n

result = 0
while start <= end:
    mid = (start + end) // 2

    if mid**2 == n:
        result = mid
        break

    elif mid**2 < n:
        start = mid + 1
    
    else:
        end = mid - 1
        result = mid

print(result)
    