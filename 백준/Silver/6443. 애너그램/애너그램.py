
N = int(input())
for _ in range(N):
    word = list(input())
    l = len(word)

    alpha = [0]*26
    for w in word:
        alpha[ord(w)-97] += 1
    
    visited = [0]*26

    result = set()


    def dfs(s, visited):
        if len(s) == l:
            result.add(s)
            return
        
        for i in range(26):
            if alpha[i] - visited[i] > 0:
                visited[i] += 1
                dfs(s+chr(i+97), visited)
                visited[i] -= 1
        

    
    dfs('', visited)

    result = sorted(list(result))

    for r in result:
        print(r)