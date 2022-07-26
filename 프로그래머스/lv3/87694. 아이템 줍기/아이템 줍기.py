# 헤메다가 남의 풀이 참고함
# 모든 좌표는 * 2 해준다. 입출력 예 1번 [3, 5] -> [4, 5] -> [4, 6] -> [3, 6] -> [2, 6] 에서 [3, 5] -> [3, 6] 사이에 [4, 5] -> [4, 6] 경로를 지나는 것을 계산하기가 어렵기 때문이다. 계산이 쉽게 2배씩 늘려 계산한다. 

from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    
    characterX = 2*characterX; characterY = 2*characterY; itemX = 2*itemX; itemY = 2*itemY;
    # 고전한 부분..!!!테두리의 좌표를 어떻게 구할 것 인가
    # 이렇게 하면 쉽게 테두리부분만 1로 남길 수 있다ㅠㅜㅠ이 쉬운 방법을 생각 못해서 1시간을...ㅠㅜㅠㅜㅠ
    board = [[0] * 101 for i in range(101)]
    for x1, y1, x2, y2 in rectangle:
        for i in range(2*x1, 2*x2+1):
            for j in range(2*y1, 2*y2+1):
                board[i][j] = 1
    for x1, y1, x2, y2 in rectangle:
        for i in range(2*x1+1, 2*x2):
            for j in range(2*y1+1, 2*y2):
                board[i][j] = 0

    
    
    visited = [[False]*101 for _ in range(101)]
    
    def bfs(a,b,board, visited):
        q = deque([(a,b)])
        visited[a][b] = 1
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        while q:
            x, y = q.popleft()
            if x == itemX and y == itemY:
                return visited[x][y]//2
            
                
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]        
                if 1 <= nx < 101 and 1 <= ny < 101 and not visited[nx][ny] and board[nx][ny] == 1:
                # nx, ny 범위 잘 잡기!! 1 <= nx <= 101로 했다가 런타임에러남..당연하지 존재하지 않는 범위이니까...
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx,ny))
    
    
    answer = bfs(characterX, characterY,board,visited)
    return answer




