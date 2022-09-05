def sosu(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(x**(0.5))+1):
            if x % i == 0:
                return False
    return True

if __name__ == "__main__":
    M = int(input())
    N = int(input())

    result = []
    for x in range(M, N+1):
        if sosu(x) == True:
            result.append(x)
    
    if not result:
        print(-1)
    else:
        print(sum(result))
        print(min(result))