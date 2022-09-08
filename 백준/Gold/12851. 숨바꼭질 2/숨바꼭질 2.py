# from collections import deque
# if __name__ == "__main__":
#     N, K = map(int, input().split())

#     visited = [False]*100001

#     def bfs(visited, start, end):
#         visited[start] = True
#         q = deque([(start, 0)])

#         m = 100000 # 최단 시간
#         cnt = 0 # 최단 시간으로 찾는 방법의 수
#         while q:
#             now, time = q.popleft()
#             n1 = now - 1
#             n2 = now + 1
#             n3 = now * 2
#             if time <= m-1:
#                 if n1 == end:
#                     m = time + 1
#                     cnt += 1
#                 elif not visited[n1] and 0 <= n1 <= 100000:
#                     visited[n1] = True
#                     q.append((n1,time+1))
                
#                 if n2 == end:
#                     m = time + 1
#                     cnt += 1
#                 elif not visited[n2] and 0 <= n2 <= 100000:
#                     visited[n2] = True
#                     q.append((n2,time+1))
                
#                 if n3 == end:
#                     m = time + 1
#                     cnt += 1
#                 elif not visited[n3] and 0 <= n3 <= 100000:
#                     visited[n3] = True
#                     q.append((n3,time+1))
        
#         return [m, cnt]
    
#     result = bfs(visited, N, K)
#     print(result[0])
#     print(result[1])

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