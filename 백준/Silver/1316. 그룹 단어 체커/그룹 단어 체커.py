
N = int(input())

words = []
for _ in range(N):
    words.append(input())

cnt = 0
for word in words:
    s = set()
    s.add(word[0])
    for i in range(1, len(word)):
        if word[i] not in s:
            s.add(word[i])
        else:
            if word[i] == word[i-1]:
                continue
            else:
                break
    else:
        cnt += 1

print(cnt)