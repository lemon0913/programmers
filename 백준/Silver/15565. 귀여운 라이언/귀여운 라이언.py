
n,k = map(int, input().split())
dolls = list(map(int, input().split()))

minL = 1000001
cnt = 0
end = 0
for start in range(n):
    while end < n and cnt < k:
        if dolls[end] == 1:
            cnt += 1
        end += 1
    
    if cnt == k:
        minL = min(minL, end-start)
    
    if dolls[start] == 1:
        cnt -= 1

if minL == 1000001:
    print(-1)
else:
    print(minL)
