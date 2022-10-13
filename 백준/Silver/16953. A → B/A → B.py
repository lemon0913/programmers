INF = int(1e9)

A, B = map(int, input().split())

result = INF
def dfs(x, cnt):
    global result

    if x == B:
        if cnt < result:
            result = cnt
        return
    elif x > B:
        return
    
    dfs(x*2, cnt+1)
    dfs(int(str(x)+'1'), cnt+1)

dfs(A, 0)


if result == INF:
    print(-1)
else:
    print(result+1) 