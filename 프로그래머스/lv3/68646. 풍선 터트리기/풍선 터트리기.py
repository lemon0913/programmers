# vscode로 돌리니까 답은 나온다..다만 슬라이싱을 계속하는 방법이라서 시간초과가 남
# from collections import deque
# def solution(a):
#     result = set()
#     q = deque([(a,False)])
    
#     def compare(arr,flag):
#         if len(arr) == 1:
#             result.add(arr[0])
#         else:
#             if flag == False:
#                 for i in range(len(arr)-1):
#                     if arr[i] < arr[i+1]:
#                         tmp1 = arr[:i]+arr[i+1:]
#                         q.append((tmp1, True))
#                         tmp2 = arr[:i+1]+arr[i+2:]
#                         q.append((tmp2, False))
#                     elif arr[i] > arr[i+1]:
#                         tmp1 = arr[:i]+arr[i+1:]
#                         q.append((tmp1, False))
#                         tmp2 = arr[:i+1]+arr[i+2:]
#                         q.append((tmp2, True))
#             else:
#                 for i in range(len(arr)-1):
#                     if arr[i] > arr[i+1]:
#                         tmp = arr[:i]+arr[i+1:]
#                     else:
#                         tmp = arr[:i+1]+arr[i+2:]
#                     q.append((tmp, True))
    

#     while q:
#         arr, flag = q.popleft()
#         compare(arr,flag)
    
    
#     return len(result)


# https://coding-lks.tistory.com/44
def solution(a):
    answer = 2
    
    if 0 <= len(a) <= 2:
        return len(a)

    left, right = a[0],a[-1]
    
    for i in range(1, len(a)-1):
        if left > a[i]:
            answer += 1
            left = a[i]
        if right > a[-1-i]:
            answer += 1
            right = a[-1-i]
    return answer if left != right else answer-1

