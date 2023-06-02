

st = input()
if len(st) < 10:
    n = len(st)
else:
    n = 9 + (len(st)-9)//2

visited = [False]*(n+1)

def dfs(idx,result):
    if idx == len(st):
        print(' '.join(map(str,result)))
        exit()
    
    # 1자리 수 체크
    num1 = int(st[idx])
    if not visited[num1]:
        visited[num1] = True
        result.append(num1)
        dfs(idx+1,result)
        result.pop()
        visited[num1] = False

    # 2자리 수 체크
    if idx + 1 < len(st):
        num2 = int(st[idx:idx+2])
        if num2 <= n and not visited[num2]:
            visited[num2] = True
            result.append(num2)
            dfs(idx+2,result)
            result.pop()
            visited[num2] = False

dfs(0,[])