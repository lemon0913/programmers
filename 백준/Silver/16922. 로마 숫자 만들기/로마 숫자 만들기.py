# 경우의 수 중에서도 중복조합으로 푸는 문제

n = int(input())
nums = [1,5,10,50]

result = set()

def dfs(s,x):
    if len(s) == n:
        result.add(sum(s))
        return
    
    for i in range(x,4):
        s.append(nums[i])
        dfs(s,i)
        s.pop()


dfs([],0)

print(len(result))
