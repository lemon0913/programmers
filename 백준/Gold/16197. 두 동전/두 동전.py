from collections import deque

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(input()))
    
    tmp = []
    # 일단 동전의 좌표를 찾기
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'o':
                tmp.append([i,j])
                
    

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    def bfs(a1, b1, a2, b2):
        q = deque([(a1,b1,a2,b2,0)])

        while q:
            x1, y1, x2, y2, c = q.popleft()
            for i in range(4):
                nx1 = x1 + dx[i]
                ny1 = y1 + dy[i]
                nx2 = x2 + dx[i]
                ny2 = y2 + dy[i]
                

                # 버튼을 10번보다 많이 눌렀다면
                if c >= 10:
                    return -1
                
                # 동전 두개 다 안 떨어졌다면
                if 0 <= nx1 < N and 0 <= ny1 < M and 0 <= nx2 < N and 0 <= ny2 < M:
                    # 벽이라면
                    if graph[nx1][ny1] == "#":
                        nx1, ny1 = x1, y1
                    if graph[nx2][ny2] == "#":
                        nx2, ny2 = x2, y2
                    q.append((nx1, ny1, nx2, ny2, c+1))
                
                # 동전 2가 떨어졌다면
                elif 0 <= nx1 < N and 0 <= ny1 < M:
                    return c+1
                
                # 동전 1이 떨어졌다면
                elif 0 <= nx2 < N and 0 <= ny2 < M:
                    return c+1

                # 동전 2개 다 떨어졌다면
                else:
                    continue
        
        return -1

    print(bfs(tmp[0][0], tmp[0][1], tmp[1][0], tmp[1][1]))