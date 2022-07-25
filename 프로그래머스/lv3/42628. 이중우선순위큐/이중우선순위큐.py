# 우선순위큐에서 최대값을 삭제하는 방법을 알게 됨

import heapq
def solution(operations):
    answer = []
    
    h = []
    for o in operations:
        if o[0] == 'I':
            heapq.heappush(h, int(o[2:]))
        else:
            if len(h) == 0: # 이 조건을 안넣어서 시간초과 남^^..하하
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


