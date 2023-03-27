# <를 만나면 flip을 False & 모은 문자열 뒤집어 넣기
# >를 만나면 frip을 True & 모은 문자열 집어넣기
# 공백을 만나면 모은 문자열 집어 넣기


str = input()

result = ''
flip = True
tmp = ''
for s in str:
    if s == '<':
        flip = False
        result += tmp[::-1]
        tmp = ''
        result += s
    elif s == '>':
        flip = True
        result += tmp
        tmp = ''
        result += s
    elif s == ' ':
        if flip:
            result += tmp[::-1]
        else:
            result += tmp
        tmp = ''
        result += s
    else:
        tmp += s

if flip:
    result += tmp[::-1]
else:
    result += tmp
print(result)        

