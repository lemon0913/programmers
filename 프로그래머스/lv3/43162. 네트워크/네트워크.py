from collections import deque
def solution(n, computers):
       
    graph = [[] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i+1].append(j+1)
    
    visited = [False]*(n+1)
    
    def bfs(flag, start):
        if not visited[start]:
            print(flag)
            visited[start] = True
            flag = True
            q = deque([start])
        
            while q:
                v = q.popleft()
                for x in graph[v]:
                    if not visited[x]:
                        visited[x] = True
                        # flag = True
                        q.append(x)
            return flag
    
    answer = 0
    for i in range(1, n+1):
        flag = False
        # bfs(flag, i)
        # if flag == True:
        if bfs(flag, i) == True:
            print(i)
            answer += 1
           
        
    return answer