

h,w = map(int, input().split())
n = int(input())
sticker = []
for _ in range(n):
    r,c = map(int, input().split())
    sticker.append((r,c))


result = 0
for i in range(n):
    for j in range(i+1,n):
        r1, c1 = sticker[i][0], sticker[i][1]
        r2, c2 = sticker[j][0], sticker[j][1]

        if (r1+r2 <= h and max(c1,c2) <= w) or (max(r1,r2) <= h and c1+c2 <= w):
            result = max(result, r1*c1 + r2*c2)
        if (c1+r2 <= h and max(r1,c2) <= w) or (max(c1,r2) <= h and r1+c2 <= w):
            result = max(result, r1*c1 + r2*c2)
        if (r1+c2 <= h and max(c1,r2) <= w) or (max(r1,c2) <= h and c1+r2 <= w):
            result = max(result, r1*c1 + r2*c2)
        if (c1+c2 <= h and max(r1,r2) <= w) or (max(c1,c2) <= h and r1+r2 <= w):
            result = max(result, r1*c1 + r2*c2)

print(result)

