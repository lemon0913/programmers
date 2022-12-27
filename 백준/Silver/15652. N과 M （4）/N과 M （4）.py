N, M = map(int, input().split())

def dfs(x,s):
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    
    for i in range(x,N+1):
            s.append(i)
            dfs(i,s)
            s.pop()

dfs(1,[])