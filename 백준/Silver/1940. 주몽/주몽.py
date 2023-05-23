n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()


l, r, cnt = 0, n-1, 0
while l < r:
    tmp = arr[l] + arr[r]

    if tmp < m:
        l += 1
    else:
        if tmp == m:
            cnt += 1
        r -= 1

print(cnt)