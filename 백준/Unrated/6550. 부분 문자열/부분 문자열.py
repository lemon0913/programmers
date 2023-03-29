
while True:
    try:
        s,t = map(str, input().split())

        visited = [False]*(len(s))

        i = 0  # t
        j = 0  # s
        while i < len(t):
            if j >= len(s):
                break
            if t[i] == s[j]:
                visited[j] = True
                j += 1
            i += 1
        
        if False not in visited:
            print('Yes')
        else:
            print('No')

    except:
        break
            