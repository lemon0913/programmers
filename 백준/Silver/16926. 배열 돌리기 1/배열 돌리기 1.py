
n,m,r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


def rotate(a,n,m):
    c = min(n,m)//2
    for i in range(c):
        tmp = a[n-1-i][i]

        for j in range(n-1-i,i,-1):
            a[j][i] = a[j-1][i]

        for j in range(i,m-1-i):
            a[i][j] = a[i][j+1]

        for j in range(i,n-1-i):
            a[j][(i+1)*(-1)] = a[j+1][(i+1)*(-1)]

        for j in range(m-1-i,i,-1):
            a[(i+1)*(-1)][j] = a[(i+1)*(-1)][j-1]
        
        a[n-1-i][i+1] = tmp

    return a

for _ in range(r):
    graph = rotate(graph,n,m)

for i in range(n):
    print(' '.join(map(str,graph[i])))



