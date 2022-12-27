N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

def dfs(x,s):
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    
    for i in range(x,N):
        # if nums[i] not in s:
            s.append(nums[i])
            dfs(i,s)
            s.pop()

dfs(0,[])