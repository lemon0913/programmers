
n,m = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
s = 0
end = 0
for start in range(n):
    while end < n and s < m:
        s += nums[end]
        end += 1
    
    if s == m:
        cnt += 1
    
    s -= nums[start]

print(cnt)