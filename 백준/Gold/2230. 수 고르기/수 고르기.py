
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()

start = 0
end = 1
result = sys.maxsize
while start < n and  end < n:
    tmp = nums[end] - nums[start]

    if tmp == m:
        result = min(result,tmp)
        break

    if tmp < m:
        end += 1
        continue
    start += 1
    result = min(result,tmp)

print(result)

    