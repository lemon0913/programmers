
h,w = map(int, input().split())
block = list(map(int, input().split()))

result = 0

for i in range(1,w-1):
    m1 = max(block[:i])
    m2 = max(block[i+1:])
    m = min(m1,m2)
    if block[i] < m:
        result += m - block[i]

print(result)

