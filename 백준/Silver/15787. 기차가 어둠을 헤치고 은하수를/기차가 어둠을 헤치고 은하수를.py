from collections import deque

N, M = map(int, input().split())

train = []
for _ in range(N):
    train.append(deque([0]*20))


for _ in range(M):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        if train[tmp[1]-1][tmp[2]-1] == 0:
            train[tmp[1]-1][tmp[2]-1] = 1
    elif tmp[0] == 2:
        if train[tmp[1]-1][tmp[2]-1] == 1:
            train[tmp[1]-1][tmp[2]-1] = 0
    elif tmp[0] == 3:
        train[tmp[1]-1][19] = 0
        train[tmp[1]-1].rotate(1)
    else:
        train[tmp[1]-1][0] = 0
        train[tmp[1]-1].rotate(-1)


result = []
for t in train:
    if t not in result:
        result.append(t)
print(len(result))

