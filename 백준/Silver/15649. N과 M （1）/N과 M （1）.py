from itertools import permutations

N, M = map(int, input().split())

arr = list(range(1, N+1))

results = list(permutations(arr,M))

for result in results:
    for r in result:
        print(r, end=' ')
    print()