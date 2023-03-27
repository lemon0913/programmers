# 경우의 수 > 조합 문제

def dfs(s,x):
    if len(s) == 6:
        print(' '.join(s))
        return
    
    for i in range(x,len(nums)):
        s.append(nums[i])
        dfs(s,i+1)
        s.pop()


while True:
    arr = list(map(str, input().split()))

    if len(arr) == 1 and arr[0] == '0':
        break
    
    nums = arr[1:]
    dfs([],0)

    print()

