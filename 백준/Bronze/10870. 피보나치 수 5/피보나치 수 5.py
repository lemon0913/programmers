def F(N):
    
    if N == 0:
        result = 0
    elif N == 1:
        result = 1
    else:
        result = F(N-1) + F(N-2)
    
    return result

if __name__ == "__main__":
    n = int(input())
    print(F(n))