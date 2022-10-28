
N, M = map(int, input().split())

nums = list(range(1, N+1))

def dfs(s):
    if len(s) == M:
        print(' '.join(list(map(str,s))))
        return
    

    for i in range(1, N+1):
        s.append(i)
        dfs(s)
        s.pop()

dfs([])