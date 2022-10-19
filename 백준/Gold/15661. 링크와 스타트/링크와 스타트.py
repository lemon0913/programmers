INF = int(1e9)

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


nums = set(range(N))


result = INF
def dfs(x,a):
    global result

    if len(a) > N//2 :
        return
    
    for i in range(x,N):
        a.append(i)

        tmp1 = 0
        for j in a:
            for k in a:
                tmp1 += graph[j][k]
        
        tmp2 = 0
        a2 = list(nums - set(a))
        for j in a2:
            for k in a2:
                tmp2 += graph[j][k]
        
        if abs(tmp1-tmp2) < result:
            result = abs(tmp1-tmp2)


        dfs(i+1, a)
        a.pop()

dfs(0,[])
print(result)