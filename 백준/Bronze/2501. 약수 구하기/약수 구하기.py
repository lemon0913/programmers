if __name__ == "__main__":
    N, K = map(int, input().split())

    cnt = 0
    i = 1
    while i <= N:
        if N % i == 0:
            cnt += 1
        if cnt == K:
            print(i)
            break
        i += 1
    else:
        print(0)