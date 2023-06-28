

# # 문자에 1)A를 추가하거나 2) B추가하고 뒤집으며 완전탐색
# # dfs 중에 문자의 길이가 T와 같아지면 확인하고 탐색 종룔

# S = input()
# T = input()

# result = 0

# def dfs(s):
#     global result

#     # S와 T의 길이가 같아지면 내용도 같아졌는지 확인하고
#     # dfs 탐색 종료
#     if len(s) == len(T):
#         if s == T:
#             result = 1
#         return
    
#     # 1) 문자에 A를 추가하고 dfs탐색
#     dfs(s+'A')

#     # 2) 문자에 B를 추가하고 뒤집은 뒤 dfs 탐색
#     s += 'B'
#     s = s[::-1]
#     dfs(s)

# dfs(S)
# print(result)

##############################################################33
# S를 T로 만드는 것은 경우의 수가 너무 많고 메모리를 많이 차지한다
# T에서 S로 만드는 과정이 훨씬 경우의 수가 적음

# 문자가 1)A로 끝나면 맨 뒤의 A를 제거 2)문자가 B로 시작하면 B를 제거하고 뒤집기
# dfs 중에 문자의 길이가 S와 같아지면 확인하고 탐색 종료

S = input()
T = input()

result = 0

def dfs(t):
    global result

    # t가 S의 길이와 같아지면 내용도 같은지 확인하고
    # dfs 탐색 종료
    if len(t) == len(S):
        if t == S:
            result = 1
        return
    
    # 1) t가 A로 끝나면 제거하고 dfs 탐색
    if t[-1] == 'A':
        dfs(t[:-1])
    
    # 2) t가 B로 시작하면 제거하고 dfs 탐색
    if t[0] == 'B':
        t = t[1:]
        t = t[::-1]
        dfs(t)

dfs(T)
print(result)
