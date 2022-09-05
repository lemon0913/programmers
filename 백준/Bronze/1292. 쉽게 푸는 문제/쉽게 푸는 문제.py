if __name__ == "__main__":
    A, B = map(int, input().split())

    arr = []
    l = 0
    i = 0
    while True:
        i += 1
        arr += [i]*i
        l += i

        if l >= B:
            break
    
    print(sum(arr[A-1:B]))
