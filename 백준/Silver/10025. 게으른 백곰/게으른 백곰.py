from collections import defaultdict
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
ice = defaultdict(int)
maxI = -1
minI = 1000001
for i in range(n):
    g,x = map(int, input().split())
    ice[x] = g
    maxI = max(maxI,x)
    minI = min(minI,x)


end = 0
s = 0
result = -1
for start in range(minI, maxI+1):
    while end < maxI+1 and end - start <= k*2:
        s += ice[end]
        end += 1
    
    result = max(result,s)
    s -= ice[start]

print(result)
    