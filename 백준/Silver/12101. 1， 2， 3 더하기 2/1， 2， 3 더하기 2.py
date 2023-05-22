
n,k = map(int, input().split())
result = []

def dfs(s,num):
    
    if num == n:
        result.append(s)
        return
    
    for i in range(1,4):
        if num + i <= n:
            dfs(s+'+'+str(i),num+i)

dfs('',0)
if len(result) < k:
    print(-1)
else:
    print(result[k-1][1:])