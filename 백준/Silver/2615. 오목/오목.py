# 고려해야할 방향이 3개가 아니라 4개다....바보야...

# graph = []
# for _ in range(19):
#     graph.append(list(map(int, input().split())))


# flag = False
# result = 0
# i = j = 0
# dx = [0,1,1,-1]
# dy = [1,0,1,1]
# for x in range(19):
#     for y in range(19):
#         if graph[x][y] != 0:
#             com = graph[x][y]
#             tx = x
#             ty = y

#             for k in range(4):
#                 cnt = 1
#                 for _ in range(4):
#                     nx = tx + dx[k]
#                     ny = ty + dy[k]
#                     if 0 <= nx < 19 and 0 <= ny < 19:
#                         if graph[nx][ny] == com:
#                             tx = nx
#                             ty = ny
#                             cnt += 1
#                         else:
#                             break
#                 if cnt == 5 and graph[tx + dx[k]][ty + dy[k]] != com:
#                     flag = True
#                     i = x
#                     j = y
#                     result = com
#                     break
#         if flag:
#             break
#     if flag:
#             break

# if result != 0:
#     print(result)
#     print(i+1,j+1)




#33333333333333333333333333333333333333333333333333######
import sys


board = []
for i in range(19):
    board.append(list(map(int, input().split())))

# → ↓ ↘ ↗
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            focus = board[x][y]

            for i in range(4):
                cnt = 1
                nx = x + dx[i]
                ny = y + dy[i]

                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == focus:
                    cnt += 1

                    if cnt == 5:
                        # 육목 체크
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x - dx[i]][y - dy[i]] == focus:
                            break
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and board[nx + dx[i]][ny + dy[i]] == focus:
                            break
                        # 육목이 아니면 성공한거니까 종료
                        print(focus)
                        print(x + 1, y + 1)
                        sys.exit(0)

                    nx += dx[i]
                    ny += dy[i]

print(0)