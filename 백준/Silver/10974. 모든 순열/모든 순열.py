
n = int(input())

def dfs(s):

    if len(s) == n:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs(s)
            s.pop()

dfs([])

