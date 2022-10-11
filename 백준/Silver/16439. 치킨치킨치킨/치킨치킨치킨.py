N, M = map(int, input().split())
prefer = []
for _ in range(N):
    prefer.append(list(map(int, input().split())))

result = 0

def dfs(s, x):
    global result

    if len(s) == 3:
        c = 0
        for i in range(N):
            c += max(prefer[i][s[0]], prefer[i][s[1]], prefer[i][s[2]])
        
        if c > result:
            result = c
        return
    
    for i in range(x, M):
        s.append(i)
        dfs(s, i+1)
        s.pop()

dfs([], 0)

print(result)