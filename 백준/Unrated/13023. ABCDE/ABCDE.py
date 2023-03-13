# 문제 조건을 이해 못함...ㅎㅎㅎㅎ > 5명 이상의 친구관계가 생겼는지를 확인하는 것
# dfs로 풀자


n,m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*n
result = False
def dfs(start, depth):
    global result

    visited[start] = True
    if depth >= 4:
        result = True
        return
    
    for x in graph[start]:
        if not visited[x]:
            visited[x] = True
            dfs(x,depth+1)
            visited[x] = False

for i in range(n):
    dfs(i,0)
    visited[i] = False
    if result:
        break

if result:
    print(1)
else:
    print(0)