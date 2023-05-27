# 연산의 범위를 못 잡겠네...

g = int(input())
be,af = 1,1 # 투포인터

result = []
while be < 100000 and af < 100000:

    tmp = af**2 - be**2

    if tmp == g:
        result.append(af)
        be += 1
    elif tmp < g:
        af += 1
    else:
        be += 1

if not result:
    print(-1)
else:
    for r in result:
        print(r)
