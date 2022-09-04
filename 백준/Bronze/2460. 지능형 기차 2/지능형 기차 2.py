if __name__ == "__main__":
    m = 0
    cnt = 0
    for _ in range(10):
        x, y = map(int, input().split())
        cnt = cnt - x + y
        if cnt > m:
            m = cnt
    print(m)