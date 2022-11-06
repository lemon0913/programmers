from itertools import combinations

N = input()

# 홀수의 개수를 찾는 함수
def find(snum): 
    cnt = 0
    for n in snum:
        if int(n)%2 == 1:
            cnt += 1
    
    return cnt


result = []
def dfs(num, c):
    if len(num) == 1:
        c += find(num)
        result.append(c)
        return
    
    elif len(num) == 2:
        c += find(num)
        num = str(int(num[0]) + int(num[1]))
        dfs(num, c)
    

    elif len(num) == 3:
        c += find(num)
        num = str(int(num[0])+int(num[1])+int(num[2]))
        dfs(num, c)
    
    else:
        c += find(str(num))
        tmp = list(range(1,len(num)))
        tmp = list(combinations(tmp, 2))

        for t in tmp:
            s = int(num[:t[0]])
            s += int(num[t[0]:t[1]])
            s += int(num[t[1]:])
            dfs(str(s),c)


dfs(N,0)
print(min(result), max(result))