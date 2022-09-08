from collections import deque
if __name__ == "__main__":
    N, K = map(int, input().split())

    visited = [-1]*100001

    def bfs(visited, start, end):
        visited[start] = 0
        q = deque([start])

        cnt = 0 # 최단 시간으로 찾는 방법의 수
        while q:
    
            x = q.popleft()
            if x == end:
                cnt += 1
            else:
                for nx in (x*2, x-1, x+1):
                    if 0 <= nx <= 100000 and (visited[nx] == -1 or visited[nx] == visited[x]+1):
                        visited[nx] = visited[x]+1
                        q.append((nx))
        
        return cnt
        
        
            
    result = bfs(visited, N, K)
    print(visited[K])
    print(result)