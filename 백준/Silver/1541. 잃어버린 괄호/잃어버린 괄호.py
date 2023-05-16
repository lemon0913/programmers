st = input()

# - 기준으로 나누기
tmp = st.split('-')
for i in range(len(tmp)):
    if '+' not in tmp[i]:
        tmp[i] = int(tmp[i])
    else:
        ttmp = tmp[i].split('+')
        s = 0
        for t in ttmp:
            s += int(t)
        tmp[i] = s

if len(tmp) == 1:
    print(tmp[0])
else:
    result = tmp[0]
    for i in range(1,len(tmp)):
        result -= tmp[i]
    print(result)
