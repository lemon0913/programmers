# 85점짜리 풀이....뭐가 틀린것인가...ㅠㅜ
# import heapq
# def solution(jobs):
#     end = 0
#     answer = 0
#     h = []
#     l = len(jobs)
      
      # jobs 배열을 작업이 요청되는 시점 기준으로 오름차순으로 정렬
#     jobs.sort(key = lambda x:x[0]) 

    
#     # 맨 처음에는 하드디스크가 작업을 수행하고 있지 않으니 가장 첫번째 요청을 일단 처리하자
#     t = jobs.pop(0)
#     end += t[0]+t[1]
#     answer += t[1]
    
#     while jobs:
        
#         if jobs[0][0] <= end or len(h) == 0:
#             t = jobs.pop(0)
#             heapq.heappush(h, (t[1], t[0]))
#         else:
#             while end <= jobs[0][0]:
#                 time, come = heapq.heappop(h)
#                 end += time
#                 answer += (end-come)
    
#     while h:
#         time, come = heapq.heappop(h)
#         end += time
#         answer += (end-come)  
        
    
#     return answer//l




# https://soohyun6879.tistory.com/136
import heapq
def solution(jobs):
    
    answer, now, i = 0, 0, 0 # now : 현재 시점
    start = -1     # 바로 이전에 작업을 완료한 시간
    heap = []
    
    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        
        if len(heap) > 0: # 처리할 작업이 있는 경우
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1] # 작업 요청시간부터 종료시간까지의 시간 계산
            i +=1
        else: # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1
                
    return answer // len(jobs)
