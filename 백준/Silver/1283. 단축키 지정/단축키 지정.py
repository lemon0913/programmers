
n = int(input())

result = []
short = []
for _ in range(n):
    word = list(map(str,input().split()))
    case = 3
    
    for j in range(len(word)):
        if word[j][0].upper() not in short and word[j][0].lower():
            short.append(word[j][0].upper())
            short.append(word[j][0].lower())
            t = '[' + word[j][0] + ']' + word[j][1:]
            word[j] = t
            result.append(word)
            case = 1
            break
    
    if case != 1:
        for j in range(len(word)):
            for i in range(1,len(word[j])):
                if word[j][i].upper() not in short and word[j][i].lower() not in short:
                    short.append(word[j][i].upper())
                    short.append(word[j][i].lower())
                    if i != len(word[j])-1:
                        t = word[j][:i] + '[' + word[j][i] + ']' + word[j][i+1:]
                        word[j] = t
                    else:
                        t = word[j][:i] + '[' + word[j][i] + ']'
                        word[j] = t
                    result.append(word)
                    case = 2
                    break
            if case == 2:
                break
    
    if case == 3:
        result.append(word)

for r in result:
    print(' '.join(r))

