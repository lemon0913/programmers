
# 투 포인터로 앞, 뒤 포인터가 가리키는 값을 비교해 추가하기

# 투 포인터가 가리키는 문자가 같을 때는 거기서 새로운 투 포인터를 사용해
# 다른 문자가 나올 떄 까지 가운데로 진행
 

n = int(input())
word = ''
for _ in range(n):
    word += input()

start = 0
end = n-1

result = ''
cnt = 0
while start <= end:
    if word[start] < word[end]:
        result += word[start]
        start += 1
    elif word[start] > word[end]:
        result += word[end]
        end -= 1
    else:
        ss, ee = start, end
        flag = False
        while ss <= ee:
            if word[ss] < word[ee]:
                result += word[start]
                start += 1
                flag = True
                break
            elif word[ss] > word[ee]:
                result += word[end]
                end -= 1
                flag = True
                break
            else:
                ss += 1
                ee -= 1
        
        if not flag:
            result += word[start]
            start += 1
    
    cnt += 1
    if cnt % 80 == 0:
        result += '\n'
    
    
print(result)