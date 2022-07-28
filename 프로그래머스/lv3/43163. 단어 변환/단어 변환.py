import heapq
def solution(begin, target, words):
    l = len(begin) # 각 단어의 길이
    
    
    
    def bfs(word,visited):
        q = []
        heapq.heappush(q,(0,word))
        
        while q:
            c, v = heapq.heappop(q)
            if v == target:
                return c
            for j in range(len(words)):
                # 한 글자만 달라서 변환할 수 있다면
                if not visited[j]:
                    for i in range(l):
                        if v[:i]+v[i+1:] == words[j][:i]+words[j][i+1:]:
                            q.append((c+1,words[j]))
                            visited[j] = True
                            print(words[j])
                            break
    
    
    
    visited = [False]*len(words)
    t = bfs(begin,visited)
    if t == None:
        return 0
    else:
        return t
    
    
