# 괄호 올바른지 확인하는건 이제 쉬운데 얘는 무슨 이상한 연산까지 있어서...
# 근데 이 이상한 연산을 실전에서 생각해내지 못할 것 같다..ㅋㅋ큐ㅜ


if __name__ == "__main__":
    arr = list(input())

    stk = []
    tmp = 1
    answer = 0

    for i in range(len(arr)):
        
        if arr[i] == '(':
            tmp *= 2
            stk.append(arr[i])
        
        elif arr[i] == '[':
            tmp *= 3
            stk.append(arr[i])

        elif arr[i] == ')':
            if not stk or stk[-1] == '[':
                answer = 0
                break
            elif arr[i-1] == '(':
                answer += tmp
            tmp //= 2
            stk.pop()
        
        else:
            if not stk or stk[-1] == '(':
                answer = 0
                break
            elif arr[i-1] == '[':
                answer += tmp
            tmp //= 3
            stk.pop()
    
    if stk:
        print(0)
    else:
        print(answer)