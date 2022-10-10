n = int(input())
switch = [-1]+list(map(str, input().split()))
s = int(input())


for _ in range(s):
    a, b = map(int, input().split())

    if a == 1:
        t = 1
        while t*b <= n:
            if switch[t*b] == '1':
                switch[t*b] = '0'
            else:
                switch[t*b] = '1'
            t += 1
        

    else:
        if switch[b] == '1':
            switch[b] = '0'
        else:
            switch[b] = '1'
        
        t = 1
        while True:
            if b-t > 0 and b+t <= n and switch[b-t] == switch[b+t]:
                if switch[b-t] == '1':
                    switch[b-t] = '0'
                    switch[b+t] = '0'
                else:
                    switch[b-t] = '1'
                    switch[b+t] = '1'
            else:
                break
            t += 1
            

for i in range(1, n+1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()