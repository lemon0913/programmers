

r,c = map(int, input().split())
# 땅의 좌표 구하기
map = [['.']*(c+2)]
ground = []
for i in range(r):
    tmp = list(input())
    tmp = ['.'] + tmp
    tmp.append('.')
    map.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] == 'X':
            ground.append((i+1,j))
map.append(['.']*(c+2))


change = []
for a,b in ground:
    # 4면이 바다
    if map[a-1][b] == '.' and map[a+1][b] == '.' and map[a][b-1] == '.' and map[a][b+1] == '.':
        change.append((a,b))
    
    # 3면이 바다
    elif map[a-1][b] == 'X' and map[a+1][b] == '.' and map[a][b-1] == '.' and map[a][b+1] == '.':
        change.append((a,b))
    elif map[a-1][b] == '.' and map[a+1][b] == 'X' and map[a][b-1] == '.' and map[a][b+1] == '.':
        change.append((a,b))
    elif map[a-1][b] == '.' and map[a+1][b] == '.' and map[a][b-1] == 'X' and map[a][b+1] == '.':
        change.append((a,b))
    elif map[a-1][b] == '.' and map[a+1][b] == '.' and map[a][b-1] == '.' and map[a][b+1] == 'X':
        change.append((a,b))



# 50년 지나서 바다로 바뀜
for a,b in change:
    map[a][b] = '.'


# 지도의 크기 수정하기
while True:
    if 'X' in map[0]:
        break
    else:
        map.pop(0)
while True:
    if 'X' in map[-1]:
        break
    else:
        map.pop()

l = len(map)
while True:
    flag = True
    for i in range(l):
        if map[i][0] == 'X':
            flag = False
    
    if flag:
        for i in range(l):
            map[i].pop(0)
    else:
        break
while True:
    flag = True
    for i in range(l):
        if map[i][-1] == 'X':
            flag = False
    
    if flag:
        for i in range(l):
            map[i].pop()
    else:
        break

for i in range(len(map)):
    print(''.join(map[i]))


