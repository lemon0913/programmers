
con = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vow = ['a','e','i','o','u']

def find(str):
    flag1 = False
    flag2 = True
    flag3 = True
    
    
    if str[0] in vow or str[1] in vow:
        flag1 = True
    
    if len(str) >= 2:
        if str[0] == str[1]:
            if str[0] == str[1] == 'e' or str[0] == str[1] == 'o':
                flag3 = True
            else:
                flag3 = False
    
    if len(str) >= 3:
        for i in range(2,len(str)):
            if str[i] in vow:
                flag1 = True
            
            if str[i] == str[i-1]:
                if str[i] == str[i-1] == 'e' or str[i] == str[i-1] == 'o':
                    flag3 = True
                else:
                    flag3 = False
            
            if ((str[i] in con) and (str[i-1] in con) and (str[i-2] in con)) or ((str[i] in vow) and (str[i-1] in vow) and (str[i-2] in vow)):
                flag2 = False
    

    if flag1 and flag2 and flag3:
        return True
    else:
        return False


while True:
    word = input()
    if word == 'end':
        break

    result = find(word)
    if result:
        print('<' + word + '> is acceptable.')
    else:
        print('<' + word + '> is not acceptable.')
