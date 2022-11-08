N = int(input())

arr = [0]*366
minVal = 366
maxVal = 0
for _ in range(N):
    a,b = map(int, input().split())
    minVal = min(a,minVal)
    maxVal = max(b,maxVal)

    for i in range(a,b+1):
        arr[i] += 1


result = 0
l = 0
m = 0
for i in range(minVal, maxVal+1):
    if arr[i] == 0:
        result += l*m
        l = 0
        m = 0
    else:
        l += 1
        m = max(m,arr[i])
result += l*m

print(result)