
n = int(input())
file = {}
for _ in range(n):
    tmp = list(map(str,input().split('.')))

    if tmp[1] not in file:
        file[tmp[1]] = 1
    else:
        file[tmp[1]] += 1

result = sorted(file.items(), key = lambda x:x[0])

for t,c in result:
    print(t, c)