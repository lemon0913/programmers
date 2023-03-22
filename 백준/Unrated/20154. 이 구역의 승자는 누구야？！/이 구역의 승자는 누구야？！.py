from copy import deepcopy

S = list(input())
dic = {'A':3, 'B':2, 'C':1, 'D':2, 'E':3, 'F':3, 'G':3, 'H':3, 'I':1, 'J':1, 'K':3, 'L':1, 'M':3, 'N':3, 'O':1, 'P':2, 'Q':2, 'R':2, 'S':1, 'T':2, 'U':1, 'V':1, 'W':2, 'X':2, 'Y':2, 'Z':1}

for i in range(len(S)):
    S[i] = dic[S[i]]

while len(S) > 1:
    result = []
    for i in range(len(S)//2):
        result.append(S[i*2]+S[i*2+1])
    if len(S) % 2 == 1:
        result.append(S[-1])

    S = deepcopy(result)

if S[0] % 2 == 1:
    print('I\'m a winner!')
else:
    print('You\'re the winner?')