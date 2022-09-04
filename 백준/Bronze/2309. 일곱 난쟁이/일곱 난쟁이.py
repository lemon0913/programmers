from itertools import combinations
if __name__ == "__main__":
    arr = []
    for _ in range(9):
        arr.append(int(input()))
    
    result = list(combinations(arr, 7))
    
    for r in result:
        if sum(r) == 100:
            r = list(r)
            r.sort()
            for i in range(7):
                print(r[i])
            break