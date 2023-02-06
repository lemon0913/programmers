

# sen = input()
# result = ''

# flag = False
# tmp1 = '' # 안 뒤집어 넣음
# tmp2 = '' # 뒤집어 넣음
# for s in sen:
#     if s == '<':
#         flag = True
#         # tmp1 += '<'
    
#     if s == '>':
#         flag = False
#         tmp1 += '>'
#         result += tmp1
#         tmp1 = ''
    
#     if flag: # 태그 안이라면?
#         tmp1 += s
    
#     if not flag: # 태그 밖이라면?
#         if s == ' ':
#             result += tmp2[::-1]
#             tmp2 = ''
#             result += ' '
        
#         elif s == '<':
#             result += tmp2[::-1]
#             tmp2 = ''

#         else:
#             tmp2 += s  

# result += tmp2[::-1]
# print(result)





sen = input()


flag = False
word = ''
result = ''

for s in sen:
    # 뒤집어서 출력
    if not flag:
        if s == '<':
            flag = True
            word += s
        
        elif s == ' ':
            word += s
            result += word
            word = ''
        else:
            word = s + word
    
    # 정상적으로 출력
    else:
        word += s
        if s == '>':
            flag = False
            result += word
            word=''

print(result+word)
