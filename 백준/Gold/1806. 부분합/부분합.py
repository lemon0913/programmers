
n,s = map(int, input().split())
nums = list(map(int, input().split()))

l = 100001
cnt = 0
end = 0
for start in range(n):
    while end < n and cnt < s:
        cnt += nums[end]
        end += 1
    
    if cnt >= s:
        l = min(l,end-start)
    cnt -= nums[start]

if l == 100001:
    print(0)
else:
    print(l)