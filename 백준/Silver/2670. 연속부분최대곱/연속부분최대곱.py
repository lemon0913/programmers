n = int(input())
nums = []
for _ in range(n):
    nums.append(float(input()))

for i in range(1,n):
    nums[i] = max(nums[i], nums[i]*nums[i-1])

print('%0.3f' % max(nums))