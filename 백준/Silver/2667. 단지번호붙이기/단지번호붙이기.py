import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    graph = []
    for i in range(N):
        graph.append(list(map(int, input().replace('\n', ''))))
    
    visited = [[False]*N for _ in range(N)]


    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y):
        global cnt
        visited[x][y] = True
        if graph[x][y] == 1:
            cnt += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == False and graph[nx][ny] == 1:
                    dfs(nx, ny)
    

    cnt = 0
    house = []

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 and visited[i][j] == False:
                dfs(i, j)
                house.append(cnt)
                cnt = 0
    
    house.sort()
    print(len(house))
    for i in house:
        print(i)