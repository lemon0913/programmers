N, M = map(int, input().split())

DNAs = []
for _ in range(N):
    DNAs.append(input())

result = ''
h = 0
words = ['A', 'C', 'G', 'T']
for i in range(M):
    cnt = [0,0,0,0]
    for j in range(N):
        if DNAs[j][i] == 'A':
            cnt[0] += 1
        elif DNAs[j][i] == 'C':
            cnt[1] += 1
        elif DNAs[j][i] == 'G':
            cnt[2] += 1
        else:
            cnt[3] += 1
    
    idx = cnt.index(max(cnt))
    result += words[idx]
    h += (N-max(cnt))

print(result)
print(h)