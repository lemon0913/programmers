
# 1부터 N까지의 카드가 순서대로 쌓임 (1이 맨 위)
# (2, K) 섞기
# 1. 밑에서부터 2^k개의 카드를 더미의 맨 위로 올리기
# 2. i번째 단계는 직전에 맨 위로 올린 카드 중에서 밑에서 2^k-i+1개 카드를 더미의 맨 위로 올리기

n = int(input())
result = list(map(int, input().split()))

# (2, K) 섞기를 수행하는 함수
def mix(s,k):
    down = []
    up = []

    # 우선 밑에서부터 2^k개의 카드 구하기
    tmp = 2**k
    cnt = 1
    for i in range(n-1,-1,-1):
        if cnt > tmp:
            down.append(s[i])
        else:
            up.append(s[i])
        cnt += 1
    
    # i번째 단계는 직전에 위로 올린 카드 중에서 밑에서 2^k-i+1개의 카드를 위로 올리기
    for i in range(2,k+2):
        tmp = 2**(k-i+1)
        for _ in range(len(up)-tmp):
            down.append(up.pop(tmp))
        
    r = down+up
    r.reverse()

    return r

# print(mix([1,2,3,4,5],2))    


def dfs(s,cnt,k):

    # (2,k) 섞기를 2번 수행한 결과가 result 리스트와 같다면 k값들 출력
    if cnt == 2:
        if s == result:
            print(k[0], k[1])
        return
    
    for i in range(1,n):
        # 2**k < n이면 (2,k) 섞기 수행
        if 2**i < n:
            ss = mix(s,i)
            k.append(i)
            dfs(ss,cnt+1,k)
            k.pop()


dfs(list(range(1,n+1)),0,[])