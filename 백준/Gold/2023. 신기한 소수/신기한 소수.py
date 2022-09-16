def find_sosu(x):
    for i in range(2, int(x**(0.5))+1):
        if x % i == 0:
            return False
    
    return True

if __name__ == "__main__":
    N = int(input())
    sosu = ['2', '3', '5', '7']
    tmp = ['1', '3', '5', '7', '9']
    result = []

    if N == 1:
        pass
    else:
        for _ in range(N-1):
            for s in sosu:
                for t in tmp:
                    x = int(s+t)
                    if find_sosu(x):
                        result.append(str(x))
            
            sosu = [] + result
            result = []
            
    
    for s in sosu:
        print(int(s))