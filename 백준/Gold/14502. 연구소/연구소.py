from collections import deque
import copy
if __name__ == "__main__":

    N, M = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    
    answer = [] # bfs를 돌릴 때 마다 0의 개수 저장하는 배열
    
    def bfs():
        q = deque()
        tmp = copy.deepcopy(graph)
        for i in range(N):
            for j in range(M):
                if tmp[i][j] == 2:
                    q.append((i,j))
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or N <= nx or ny < 0 or M <= ny:
                    continue
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = 2
                    q.append((nx,ny))

        # 0의 개수 세기
        cnt = 0
        for i in range(N):
            cnt += tmp[i].count(0)
        answer.append(cnt)

        # x 다른 bfs 연산을 위해 x 초기화
        x = 0
    
    
    
    # 벽을 세우는 함수
    ####### 이 부분이 이해 안됨...........########
    def wall(x):
        if x == 3:
            bfs()
            return
        
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    wall(x+1)
                    graph[i][j] = 0


    wall(0)
    print(max(answer))