
n = int(input())
cnt = 0
end = 1
s = 0
for start in range(1,n+1):
	while s < n and end <=n:
		s += end
		end += 1
	
	if s == n:
		cnt += 1
	
	s -= start

print(cnt)
