t = int(input())
for _ in range(t):
    st = input()

    visited = [0]*26
    for s in st:
        if s != ' ':
            visited[ord(s)-ord('a')] += 1
    
    m = max(visited)

    if visited.count(m) >= 2:
        print('?')
    else:
        print(chr(ord('a')+visited.index(m)))