N = int(input())

arr = []
for _ in range(N*N):
    arr.append(list(map(int, input().split())))

graph = [[0]*N for _ in range(N)]

graph[1][1] = arr[0][0]
visited = {} # 학생의 좌표를 저장
visited[arr[0][0]] = (1,1)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(1, N*N):
    fav = arr[i][1:5]
    dic = {}
    for x in range(N):
        for y in range(N):
            fav_c = 0
            emp_c = 0
            if graph[x][y] == 0:
                for j in range(4):
                    nx = x + dx[j]
                    ny = y + dy[j]
                    if 0 <= nx < N and 0 <= ny < N:
                        if graph[nx][ny] in fav:
                            fav_c += 1
                        if graph[nx][ny] == 0:
                            emp_c += 1
            
                dic[(x,y)] = (fav_c, emp_c)
    
    
    result = sorted(dic.items(), key = lambda x:(-x[1][0], -x[1][1], x[0][0], x[0][1]))
    x, y = result[0][0]
    graph[x][y] = arr[i][0]
    visited[arr[i][0]] = (x,y)


answer = 0
scores = [0, 1, 10, 100, 1000]
for a in arr:
    c = 0
    now = a[0]
    fav = a[1:5]
    x, y = visited[now]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] in fav:
                c += 1
    answer += scores[c]

print(answer)