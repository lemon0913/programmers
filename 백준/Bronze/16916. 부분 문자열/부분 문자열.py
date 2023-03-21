


def kmp_table(p):
    lp = len(p)
    tb = [0]*lp

    j = 0
    for i in range(1,lp):
        while j > 0 and p[i] != p[j]:
            j = tb[j-1]
        
        if p[i] == p[j]:
            j += 1
            tb[i] = j
    
    return tb


def kmp(s,p):
    tb = kmp_table(p)

    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = tb[j-1]
        
        if s[i] == p[j]:
            j += 1
            if j == len(p):
                return True   
    
    return False

s = input()
p = input()

if kmp(s,p):
    print(1)
else:
    print(0)