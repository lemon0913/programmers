n = int(input())
nums = list(map(int, input().split()))
x = int(input())
nums.sort()

start = 0
end = n-1
cnt = 0
while True:
	if start >= end:
		break
	
	if nums[start] + nums[end] == x:
		start += 1
		end -= 1
		cnt += 1
	elif nums[start] + nums[end] < x:
		start += 1
	else:
		end -= 1

print(cnt)