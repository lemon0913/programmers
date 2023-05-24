n,k = map(int, input().split())
tmp = list(map(int, input().split()))

s = sum(tmp[:k])
maxV = s
for i in range(1,n-(k-1)):
	s -= tmp[i-1]
	s += tmp[i+k-1]
	maxV = max(maxV,s)
print(maxV)