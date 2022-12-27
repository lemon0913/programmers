N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

def dfs(s):
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    
    for i in range(N):
        # if nums[i] not in s:
            s.append(nums[i])
            dfs(s)
            s.pop()

dfs([])
