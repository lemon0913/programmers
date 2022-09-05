if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for a in arr:
        if a == 1:
            continue
        else:
            for i in range(2, int(a**(0.5))+1):
                if a % i == 0:
                    break
            else:
                cnt += 1
    
    print(cnt)