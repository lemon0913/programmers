INF = int(1e9)

N = int(input())

taste = []
for _ in range(N):
    taste.append(list(map(int, input().split())))

result = INF
def dfs(i, s, b, c):
    global result

    if c == N:
        return
    
    for j in range(i, N):
        s *= taste[j][0]
        b += taste[j][1]
        if abs(s-b) < result:
            result = abs(s-b)
        dfs(j+1, s, b, c+1)
        s //= taste[j][0]
        b -= taste[j][1]

dfs(0, 1, 0, 0)

print(result)
