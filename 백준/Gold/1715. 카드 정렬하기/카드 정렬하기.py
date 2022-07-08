import heapq
import sys
if __name__ == "__main__":
    N = int(input())

    heap = []
    for i in range(N):
        heapq.heappush(heap, int(sys.stdin.readline()))
    
    result = 0
    while len(heap) != 1:
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        s = x + y
        result += s
        heapq.heappush(heap, s)
        
    print(result)
