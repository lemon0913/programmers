import sys

t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()

    start = 0
    end = n-1
    x = sys.maxsize
    cnt = 0
    while start < end:
        tmp = nums[start] + nums[end]
        
        if tmp > k:
            end -= 1
        else:
            start += 1
        
        if abs(tmp - k) < x:
            x = abs(tmp-k)
            cnt = 1
        elif abs(tmp-k) == x:
            cnt += 1

    print(cnt)
        