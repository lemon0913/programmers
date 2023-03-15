# 경우의 수 조합
n = int(input())
color = []
for _ in range(n):
    color.append(list(map(int, input().split())))
gom = list(map(int, input().split()))

result = int(1e9)
def dfs(r,g,b,x,depth):
    global result

    if 2 <= depth <= 7:
        rr = sum(r)//depth
        rg = sum(g)//depth
        rb = sum(b)//depth
        result = min(result, abs(rr-gom[0])+abs(rg-gom[1])+abs(rb-gom[2]))
        # print(rr,rg,rb,result)

    if depth == 8:
        return
    
    for i in range(x,n):
        r.append(color[i][0])
        g.append(color[i][1])
        b.append(color[i][2])
        dfs(r,g,b,i+1,depth+1)
        r.pop()
        g.pop()
        b.pop()
        


dfs([],[],[],0,0)
print(result)