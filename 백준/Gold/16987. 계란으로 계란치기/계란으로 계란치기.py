# 문제 상황 이해가 너무 어렵다...

n = int(input())
eggs = []
for _ in range(n):
    eggs.append(list(map(int, input().split())))

result = 0


def check(eggs):
    cnt = 0
    for egg in eggs:
        if egg[0] <= 0:
            cnt += 1
    return cnt

def dfs(idx,eggs):
    global result

    if idx == n:
        result = max(result,check(eggs))
        return
    
    # 현재 계란의 내구도가 닳았다면 다음 계란으로 넘어가기
    if eggs[idx][0] <= 0:
        dfs(idx+1,eggs)
    # 현재 계란의 내구도가 남아있다면 다른 계란과 부딪치기
    # (현재 계란과 내구도가 닳은 계란은 제외)
    else:
        is_all_broken = True
        for i in range(n):
            if i != idx and eggs[i][0] > 0:
                is_all_broken = False
                eggs[idx][0] -= eggs[i][1]
                eggs[i][0] -= eggs[idx][1]
                dfs(idx+1,eggs) 
                eggs[idx][0] += eggs[i][1]
                eggs[i][0] += eggs[idx][1]
        # 모든 계란이 깨져있는 경우 dfs를 바로 빠져나오기
        if is_all_broken:
            dfs(n,eggs)


dfs(0,eggs)
print(result)