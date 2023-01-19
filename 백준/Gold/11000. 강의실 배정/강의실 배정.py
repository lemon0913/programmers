# 이렇게 하면 답은 나오는것 같은데...시간초과...

# n = int(input())

# time = []
# for _ in range(n):
#     time.append(list(map(int, input().split())))

# time.sort(key = lambda x:(x[1], x[0]))

# visited = [False]*(n)

# cnt = 0
# while True:
#     if False not in visited:
#         break
    
#     idx = 0
#     end = 0
#     for i in range(n):
#         if not visited[i] :
#             visited[i] = True
#             idx = i
#             end = time[i][1]
#             cnt += 1
#             break
    
#     for j in range(idx+1,n):
#         if not visited[j] and time[j][0] >= end:
#             visited[j] = True
#             end = time[j][1]

# print(cnt)

########################################################

# heapq를 사용한 풀이법
import heapq

n = int(input())
time = []
for _ in range(n):
    time.append(list(map(int, input().split())))

time.sort(key = lambda x:(x[0]))

q = []
heapq.heappush(q,time[0][1])
for i in range(1,n):
    if time[i][0] >= q[0]:
        heapq.heappop(q)
        heapq.heappush(q,time[i][1])
    else:
        heapq.heappush(q,time[i][1])

print(len(q))