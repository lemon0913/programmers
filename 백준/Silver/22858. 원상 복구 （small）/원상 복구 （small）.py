from copy import deepcopy

n,k = map(int, input().split())
S = list(map(int, input().split()))
D = list(map(int, input().split()))
S = [0] + S
D = [0] + D


for _ in range(k):
    result = [0]*(n+1)

    for i in range(1,n+1):
        result[D[i]] = S[i]
    
    S = deepcopy(result)

for i in range(1,n+1):
    print(result[i], end=' ')
