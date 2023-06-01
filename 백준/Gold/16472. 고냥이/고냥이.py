n = int(input())
st = input()
ls = len(st)
dic = {}

start = 0
cnt = 0
for end in range(ls):
    if st[end] not in dic:
        dic[st[end]] = 1
    else:
        dic[st[end]] += 1

    while len(dic) > n:
        dic[st[start]] -= 1
        if dic[st[start]] == 0:
            del dic[st[start]]
        start += 1
    
    cnt = max(cnt, end-start+1)

print(cnt)