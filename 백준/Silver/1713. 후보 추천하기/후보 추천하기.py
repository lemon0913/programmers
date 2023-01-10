
n = int(input())
m = int(input())
recom = list(map(int, input().split()))

stu = []
cnt = [0]*(101)

for r in recom:
    if r in stu:
        cnt[r] += 1
    else:
        if len(stu) < n:
            stu.append(r)
            cnt[r] = 1
        elif len(stu) == n:
            tmp = []
            for s in stu:
                tmp.append((cnt[s],s))
            tmp.sort(key = lambda x:x[0])
            cnt[tmp[0][1]] = 0
            stu.remove(tmp[0][1])

            stu.append(r)
            cnt[r] = 1
    

stu.sort()
print(' '.join(map(str,stu)))
