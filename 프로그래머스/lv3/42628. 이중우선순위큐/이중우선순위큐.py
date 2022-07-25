# 우선순위큐에서 최대값을 삭제하는 방법을 알게 됨
# 66.7점짜리 -> 아무래도 최대값을 삭제할 때마다 슬라이싱이나 heappify같은 연산을 계속 해서 그런듯
# 이건 우선순위큐를 2개 운영하면 시간초과를 막을 수 있다

import heapq
def solution(operations):
    answer = []
    
    h = []
    for o in operations:
        if o[0] == 'I':
            heapq.heappush(h, int(o[2:]))
        else:
            if len(h) == 0:
                continue
            elif o[2] == '-':
                # 최솟값 삭제
                heapq.heappop(h)
            else:
                # 최댓값 삭제
                h = heapq.nlargest(len(h), h)[1:]
                heapq.heapify(h)
    
    if len(h) == 0:
        answer = [0,0]
    elif len(h) == 1:
        t = heapq.heappop(h)
        answer = [t,t]
    else:
        t1 = heapq.heappop(h)
        t2 = heapq.nlargest(1,h)[0]
        answer = [t2,t1]
    
    return answer


# import heapq
# def solution(operations):
    
#     minh = []
#     maxh = []
#     for o in operations:
#         if o[0] == 'I':
#             heapq.heappush(minh, int(o[2:]))
#             heapq.heappush(maxh, int(o[2:]))
#         elif o[2] == '-':
#             # 최솟값 삭제
#             heapq.heappop(h)
#         else:
#             # 최댓값 삭제
#             h = heapq.nlargest(len(h), h)[1:]
#             heapq.heapify(h)
    
#     if len(h) == 0:
#         answer = [0,0]
#     elif len(h) == 1:
#         t = heapq.heappop(h)
#         answer = [t,t]
#     else:
#         t1 = heapq.heappop(h)
#         t2 = heapq.nlargest(1,h)[0]
#         answer = [t2,t1]
    
#     return answer