

def right(m):
    global n
    tmp = [0]*n

    t = n//2
    for i in range(n):
        tmp[i] = m[t][i]
    
    # 1. 부 대각선을 가운데 행으로
    for i in range(n):
        m[t][i] = m[n-1-i][i]
    
    # 2. 가운데 열을 부 대각선으로
    for i in range(n):
        m[i][n-1-i] = m[i][t]
    
    # 3. 주 대각선을 가운데 열로
    for i in range(n):
        m[i][t] = m[i][i]
    
    # 4. 가운데 행을 주 대각선으로
    for i in range(n):
        m[i][i] = tmp[i]
    

def left(m):
    global n
    tmp = [0]*n

    t = n//2
    for i in range(n):
        tmp[i] = m[t][i]
    
    # 1. 주 대각선을 가운데 행으로
    for i in range(n):
        m[t][i] = m[i][i]
    
    # 2. 가운데 열을 주 대각선으로
    for i in range(n):
        m[i][i] = m[i][t]
    
    # 3. 부 대각선을 가운데 열로
    for i in range(n):
        m[i][t] = m[i][n-1-i]

    # 4. 가운데 행을 부 대각선으로
    for i in range(n):
        m[n-1-i][i] = tmp[i]
    
    
    
T = int(input())   

for _ in range(T):
    n, d = map(int, input().split())
    
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    
    
    c = d // 45

    if c < 0:
        c = c*(-1)
        for _ in range(c):
            left(matrix)
        
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=' ')
            print()
        
    else:
        for _ in range(c):
            right(matrix)
        
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=' ')
            print()
