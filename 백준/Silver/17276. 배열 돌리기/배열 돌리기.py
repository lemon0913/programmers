
def right(graph,c,n):
    for _ in range(c):
        nn = n//2

        # 1)주대각선의 값 임시 저장하기
        tmp = [0]*(n)
        for i in range(n):
            tmp[i] = graph[i][i]
        
        # 2)가운데 행의 값을 주대각선에 집어넣기
        for i in range(n):
            graph[i][i] = graph[nn][i]
        
        # 3)부대각선의 값을 가운데 행에 집어넣기
        for i in range(n):
            graph[nn][i] = graph[n-1-i][i]
        
        # 4)가운데 열의 값을 부대각선에 집어넣기
        for i in range(n): 
            graph[n-1-i][i] = graph[n-1-i][nn]
        
        # 5)임시 저장한 값을 가운데 열에 집어 넣기
        for i in range(n):
            graph[i][nn] = tmp[i]
    


def left(graph,c,n):
    for _ in range(c):
        nn = n//2

        # 1) 주대각선의 값을 임시 저장하기
        tmp = [0]*(n)
        for i in range(n):
            tmp[i] = graph[i][i]
        
        # 2) 가운데 열의 값을 주대각선에 집어넣기
        for i in range(n):
            graph[i][i] = graph[i][nn]
        
        # 3) 부대각선의 값을 가운데 열에 집어 넣기
        for i in range(n):
            graph[i][nn] = graph[i][n-1-i]
        
        # 4) 가운데 행의 값을 부대각선에 집어넣기
        for i in range(n):
            graph[n-1-i][i] = graph[nn][i]
        
        # 5) 임지 저장한 값을 가운데 행에 집어넣기
        for i in range(n):
            graph[nn][i] = tmp[i]
    



t = int(input())
for _ in range(t):
    
    n,d = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    

    if d > 0:
        c = d//45
        right(graph,c,n)
    
    elif d < 0:
        c = d*(-1)//45
        left(graph,c,n)
    

    for i in range(n):
        print(' '.join(map(str,graph[i])))