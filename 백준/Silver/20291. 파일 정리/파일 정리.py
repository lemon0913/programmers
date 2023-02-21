n = int(input())
dic = {}
for _ in range(n):
    a,b = input().split('.')

    if b not in dic:
        dic[b] = 1
    else:
        dic[b] += 1

result = sorted(dic.items(), key = lambda x:x[0])

for r in result:
    print(r[0], r[1])