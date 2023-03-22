
# 부분문자열...KMP 알고리즘은 진짜 잘 알고 있어야겠다..
S = input()
K = input()

word = ''
for s in S:
    if 'a' <= s <= 'z' or 'A' <= s <= 'Z':
        word += s



def kmp_list(pattern):
    lp = len(pattern)
    tb = [0]*lp

    j = 0
    for i in range(1,lp):
        while j > 0 and pattern[i] != pattern[j]:
            j = tb[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            tb[i] = j
    
    return tb

def kmp(word,pattern):
    tb = kmp_list(pattern)

    j = 0
    for i in range(len(word)):
        while j > 0 and word[i] != pattern[j]:
            j = tb[j-1]
        if word[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                return 1
    
    return 0

print(kmp(word,K))