

n,m = map(int, input().split())
hear = set()
for _ in range(n):
    hear.add(input())
see = set()
for _ in range(m):
    see.add(input())

result = hear & see
result = list(result)
result.sort()
print(len(result))
for r in result:
    print(r)