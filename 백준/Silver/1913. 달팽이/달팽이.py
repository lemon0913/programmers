
n = int(input())
x = int(input())


result = [[0]*n for _ in range(n)]

l = n - 1
c = 0
num = n*n
while l > 0:
    
    # 1
    for i in range(l):
        result[c+i][c] = num
        num -= 1

    # 2
    for i in range(l):
        result[n-1-c][c+i] = num
        num -= 1
    
    # 3
    for i in range(l):
        result[n-1-c-i][n-1-c] = num
        num -= 1
    
    # 4
    for i in range(l):
        result[c][n-1-c-i] = num
        num -= 1
    
    l -= 2
    c += 1

result[n//2][n//2] = 1


for i in range(n):
    print(' '.join(map(str,result[i])))

a = b = -1
flag = False
for i in range(n):
    if x in result[i]:
        b = result[i].index(x)
        a = i
        flag = True
        break
    
    if flag:
        break
print(a+1, b+1)
