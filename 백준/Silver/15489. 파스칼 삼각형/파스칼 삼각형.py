
r,c,w = map(int, input().split())

graph = []
for i in range(1,r+w):
    graph.append([1]*i)

for i in range(1,r+w-1):
    if i == 1:
        continue
    
    for j in range(1,i):
        graph[i][j] = graph[i-1][j-1] + graph[i-1][j]

cnt = 0
r -= 1
c -= 1
for i in range(w):
    for j in range(i+1):
        cnt += graph[r+i][c+j]
print(cnt)

