# 문제를 잘 읽자! four이 제목에 붙은 이유는 넷 이하의 제곱수의 합으로 표현하기 때문!!
# dfs로 풀어보려 했으나 잘 안됨.....

# n = int(input())


# z = int(n**(0.5))

# result = 5
# def dfs(depth,s,x,l):
#     global result

#     if x == 0:
#         result = min(result,depth)
#         print(l)
#         return
    
#     for i in range(1,s+1):
#         t = x-i*i
#         if t >= 0 and depth < 4:
#             l.append(i)
#             dfs(depth+1,int(i**(0.5)),t,l)
#             l.pop()

# dfs(0,z,n,[])


# print(result)

#####################################################

# 원래는 dp로 푸는 것이 정석인 듯 하다.....


import math
 
def fourSquares(n):
    # √n이 정수일 때
    if int(math.sqrt(n)) == math.sqrt(n):
        return 1
    # √(n - i^2)이 정수일 때
    for i in range(1, int(math.sqrt(n)) + 1):
        if int(math.sqrt(n - i**2)) == math.sqrt(n - i**2):
            return 2
    # √(n - i^2 - j^2)이 정수일 때
    for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(1, int(math.sqrt(n - i**2)) + 1):
            if int(math.sqrt(n - i**2 - j**2)) == math.sqrt(n - i**2 - j**2):
                return 3
    # 남은 경우는 4
    return 4
 
 
n = int(input())
print(fourSquares(n))
