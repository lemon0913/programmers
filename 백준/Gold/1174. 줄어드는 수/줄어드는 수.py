# 백트래킹도 가능하고 조합도 가능하다

N = int(input())


result = []
def dfs(s,x):
    if len(s) > 10:
        return
    
    for i in range(x,-1,-1):
        s += str(i)
        result.append(int(s))
        dfs(s,i-1)
        s = s[:-1]
        

dfs('',9)

result.sort()


if N > len(result):
    print(-1)
else:
    print(result[N-1])
