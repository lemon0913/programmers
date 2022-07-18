# https://gurumee92.tistory.com/164
def solution(N, number):
    answer = -1
    DP = []

    for i in range(1,9):
        numbers = set()
        numbers.add( int(str(N) * i) ) # 각 set마다 기본 수 "N" * i 수 초기화
        
        
        for j in range(0, i-1):
            for x in DP[j]:
                for y in DP[-j-1]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)
                    
                    if y != 0:
                        numbers.add(x // y)
        
        if number in numbers:
            return i
        else:
            DP.append(numbers)
            
                    
    
    return answer