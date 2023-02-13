

n,m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def dfs(s):

    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(n):
        if nums[i] not in s:
            s.append(nums[i])
            dfs(s)
            s.pop()

dfs([])
