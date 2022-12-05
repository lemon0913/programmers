N = int(input())
stu = []
for _ in range(N*N):
    stu.append(list(map(int, input().split())))

graph = [[0]*N for _ in range(N)]

graph[1][1] = stu[0][0]

dx = [0,0,-1,1]
dy = [1,-1,0,0]
for i in range(1,N*N):
    like = stu[i][1:]

    # 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸 구하기
    tmp = []
    m = 0
    for x in range(N):
        for y in range(N):
            if graph[x][y] == 0:
                cnt = 0
                for a in range(4):
                    nx = x + dx[a]
                    ny = y + dy[a]
                    if 0 <= nx < N and 0 <= ny < N:
                        if graph[nx][ny] in like:
                            cnt += 1              
                m = max(m,cnt)
                tmp.append((x,y,cnt))
    near = []
    for a in range(len(tmp)):
        if tmp[a][2] == m:
            near.append((tmp[a][0],tmp[a][1]))
    
    # 좋아하는 학생이 인접한 칸에 가장 많은 칸의 갯수가 1개라면 조건에 1에 의해 결정남
    if len(near) == 1:
        graph[near[0][0]][near[0][1]] = stu[i][0]
    else: # 2개 이상이라면 조건 2에 의해 판별해야 함
        # 1을 만족하는 칸 중에서 비어있는 칸이 가장 많은 칸 구하기
        tmp = []
        m = 0
        for x,y in near:
            cnt = 0
            for a in range(4):
                nx = x + dx[a]
                ny = y + dy[a]
                if 0 <= nx < N and 0 <= ny < N:
                    if graph[nx][ny] == 0:
                        cnt += 1
            m = max(m,cnt)
            tmp.append((x,y,cnt))
        
        # empty = []
        # for a in range(len(tmp)):
        #     if tmp[a][2] == m:
        #         empty.append((tmp[a][0], tmp[a][1]))
        
        # # 빈 칸이 인접한 칸에 가장 많은 칸의 갯수가 1개라면 조건 2에 의해 결정남
        # if len(empty) == 1:
        # graph[empty[0][0]][empty[0][1]] = str[i][0]
        for a in range(len(tmp)):
            if tmp[a][2] == m:
                graph[tmp[a][0]][tmp[a][1]] = stu[i][0]
                break
        


stu.sort(key = lambda x:x[0])

sm = 0
score = [0,1,10,100,1000]
for x in range(N):
    for y in range(N):
        s = graph[x][y]
        like = stu[s-1][1:]
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] in like:
                    cnt += 1
        sm += score[cnt]

print(sm)