from itertools import combinations

N, M = map(int, input().split())
chicken = []
house = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 1:
            house.append((i,j))
        elif tmp[j] == 2:
            chicken.append((i,j))

chicken = list(combinations(chicken,M))
result = []

for chi in chicken:
    s = 0
    for h in house:
        dis = int(1e9)
        for c in chi:
            dis = min(dis, abs(c[0]-h[0])+abs(c[1]-h[1]))
        s += dis
    result.append(s)

print(min(result))