# 테두리 4면을 돌아가면서 채우면 됨

n = int(input())
x = int(input())

graph = [[0]*n for _ in range(n)]


i = 0
l = n-1
nn = n*n
while nn > 1:

    # 왼쪽 면
    for j in range(l):
        graph[i+j][i] = nn
        nn -= 1


    # 아랫 면
    for j in range(l):
        graph[n-1-i][i+j] = nn
        nn -= 1


    # 오른쪽 면
    for j in range(l):
        graph[n-1-i-j][n-1-i] = nn
        nn -= 1


    # 윗 면
    for j in range(l):
        graph[i][n-1-i-j] = nn
        nn -= 1

    i += 1
    l -= 2

graph[n//2][n//2] = 1

a = b = 0
for i in range(n):
    tmp = graph[i]
    if x in tmp:
        a = i
        b = tmp.index(x)
    print(' '.join(map(str,tmp)))

print(a+1,b+1)