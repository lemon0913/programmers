# 참고자료 : https://esoongan.tistory.com/71
import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    minH = []
    maxH = []
    visited = [False]*(1000001)

    k = int(input())
    for i in range(k):
        order, num = map(str, input().split())
        if order == 'I':
            heapq.heappush(minH, (int(num),i))
            heapq.heappush(maxH,(int(num)*(-1),i))
            visited[i] = True # True면 아직 어떤 힙에서도 삭제되지 않음

        else:
            if num == '-1': # 삭제 연산 시, i값을 기준으로 해당 노드가 다른 힙에서 삭제된 것인지 확인
                while minH and not visited[minH[0][1]]:
                    heapq.heappop(minH)
                if minH:
                    visited[minH[0][1]] = False
                    heapq.heappop(minH)
            else:
                while maxH and not visited[maxH[0][1]]:
                    heapq.heappop(maxH)
                if maxH:
                    visited[maxH[0][1]] = False
                    heapq.heappop(maxH)
    
    # 모든 연산이 끝난 후에도 쓰레기 노드가 들어있을 수 있으니, 결과를 내기 전 모두  비우고 각 힙의 첫번째 원소 출력
    while minH and not visited[minH[0][1]]:
        heapq.heappop(minH)
    while maxH and not visited[maxH[0][1]]:
        heapq.heappop(maxH)
    
    if minH and maxH:
        print(-maxH[0][0], minH[0][0])
    else:
        print('EMPTY')