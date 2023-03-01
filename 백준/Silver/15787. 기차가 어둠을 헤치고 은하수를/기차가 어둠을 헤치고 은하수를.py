

# 1 i x : i번째 기차 x번째 좌석에 사람을 태우기 > 사람이 이미 있다면 아무일도 x
# 2 i x : i번째 기차 x번째 좌석에 사람 내리기 > 사람이 이미 없다면 아무일도 x
# 3 i : i번째 기차에 앉은 승객 모두 한칸씩 뒤로! 20번째 자리에 사람이 있다면 그 사람은 하차함
# 4 i : i번째 기차에 앉은 승객 모두 한칸씩 앞으로! 1번째 자리에 앉은 사람이 있다면 하차하기
from collections import deque

n,m = map(int, input().split())
trains = []
for _ in range(n):
    trains.append(deque([False]*(20)))

for _ in range(m):
    tmp = list(map(int, input().split()))

    # 1 i x
    if tmp[0] == 1:
        trains[tmp[1]-1][tmp[2]-1] = True
    # 2 i x
    elif tmp[0] == 2:
        trains[tmp[1]-1][tmp[2]-1] = False
    # 3 i
    elif tmp[0] == 3:
        trains[tmp[1]-1][-1] = False
        trains[tmp[1]-1].rotate(1)
    # 4 i
    elif tmp[0] == 4:
        trains[tmp[1]-1][0] = False
        trains[tmp[1]-1].rotate(-1)

result = []
for i in range(n):
    if trains[i] not in result:
        result.append(trains[i])

print(len(result))

