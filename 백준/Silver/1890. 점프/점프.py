if __name__ == "__main__":
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    

    visited = [[0]*N for _ in range(N)]
    visited[0][0] = 1
    
    for i in range(N):
        for j in range(N):
            if i == N-1 and j == N-1:
                break

            t = graph[i][j]
            if i + t < N:
                visited[i+t][j] += visited[i][j]
            if j + t < N:
                visited[i][j+t] += visited[i][j]
    
    print(visited[N-1][N-1])