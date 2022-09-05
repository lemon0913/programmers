if __name__ == '__main__':
    N = int(input())
    graph = []
    for i in range(N):
        graph.append(list(map(str, input())))
    
    s = set()
    result = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x in range(N):
        for y in range(N):
            for i in range(4):
                if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N:
                    if (x,y,x+dx[i],y+dy[i]) in s:
                        continue
                    else:
                        s.add((x, y, x+dx[i], y+dy[i]))
                        s.add((x+dx[i], y+dy[i], x, y))

                        graph[x][y], graph[x+dx[i]][y+dy[i]] = graph[x+dx[i]][y+dy[i]], graph[x][y]

                        m = 0
                        for a in range(N):
                            cnt = 1
                            for b in range(N-1):
                                if graph[a][b] == graph[a][b+1]:
                                    cnt += 1
                                else:
                                    m = max(m, cnt)
                                    cnt = 1
                            m = max(m, cnt)
                        
                        for a in range(N):
                            cnt = 1
                            for b in range(N-1):
                                if graph[b][a] == graph[b+1][a]:
                                    cnt += 1
                                else:
                                    m = max(m, cnt)
                                    cnt = 1
                            m = max(m, cnt)
                        
                        result.append(m)
                        graph[x][y], graph[x+dx[i]][y+dy[i]] = graph[x+dx[i]][y+dy[i]], graph[x][y]
    
    print(max(result))