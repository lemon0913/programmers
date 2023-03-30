
n = int(input())
nums = list(map(int, input().split()))

answer = 0

def dfs(s):
    global answer

    if len(s) == n:
        result = 0
        for i in range(n-1):
            result += abs(nums[s[i]] - nums[s[i+1]])
        answer = max(answer,result)
        return
    

    for i in range(n):
        if i not in s:
            s.append(i)
            dfs(s)
            s.pop()

dfs([])
print(answer)
