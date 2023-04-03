
s = input()
result = []
tmp = ''
for i in range(len(s)-1,-1,-1):
    tmp = s[i] + tmp
    result.append(tmp)

result.sort()
for r in result:
    print(r)