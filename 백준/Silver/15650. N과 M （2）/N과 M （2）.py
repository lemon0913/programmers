
N, M = map(int, input().split())

nums = list(range(1, N+1))

def dfs(s, x):
    if len(s) == M:
        print(' '.join(list(map(str,s))))
    

    for i in range(x, N+1):
        s.append(i)
        dfs(s,i+1)
        s.pop()

dfs([],1)