N, S = map(int, input().split())

nums = list(map(int, input().split()))

result = 0
def dfs(s, x):
    global result
    
    if len(s) == N:
        return
    
    for i in range(x, N):
        s.append(nums[i])
        if sum(s) == S:
            result += 1
        dfs(s, i+1)
        s.pop()

dfs([], 0)
print(result)