# 시간초과남...처음에 생각한 방법이 맞았음...
# r,s = map(int, input().split())

# photo = []
# for i in range(r):
#     photo.append(list(input()))

# ground = [-1]*s

# for i in range(s):
#     for j in range(r):
#         if photo[j][i] == '#':
#             ground[i] = j-1
#             break



# flag = True 
# while True:
#     for i in range(s):
#         if ground[i] < 0:
#             pass
#         else:
#             if photo[ground[i]][i] == 'X':
#                 flag = False
#                 break
    
#     if not flag:
#         break
    
#     for i in range(s):
#         if ground[i] < 0:
#             pass
#         else:
#             for j in range(ground[i]-1,-1,-1):
#                 photo[j+1][i] = photo[j][i]
#             photo[0][i] = '.'

# for i in range(r):
#     print(''.join(photo[i]))


INF = int(1e9)
r,s = map(int, input().split())

photo = []
for i in range(r):
    photo.append(list(input()))

result = [['.']*s  for _ in range(r)]

star = [INF*(-1)]*s
ground = [INF]*s

for i in range(s):
    for j in range(r):
        if photo[j][i] == 'X':
            star[i] = max(star[i],j)
        elif photo[j][i] == '#':
            ground[i] = min(ground[i], j)


cnt = INF
for i in range(s):
    cnt = min(cnt, ground[i]-star[i])
cnt -= 1

for i in range(r):
    for j in range(s):
        if photo[i][j] == 'X':
            result[i+cnt][j] = 'X'
        elif photo[i][j] == '#':
            result[i][j] = '#'

for i in range(r):
    print(''.join(result[i]))