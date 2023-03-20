# 1,4,7 > 왼손
# 3,6,9 > 오른손
# 2,5,8,0 > 더 가까운 손 > 거리가 같다면 잡이손으로
def solution(numbers, hand):
    answer = ''
    visited = [[False]*3 for _ in range(4)]
    
    left = [-1,1,-1,-1,4,-1,-1,7]
    left_po = [-1,[0,0],-1,-1,[1,0],-1,-1,[2,0]]
    right = [-1,-1,-1,3,-1,-1,6,-1,-1,9]
    right_po = [-1,-1,-1,[0,2],-1,-1,[1,2],-1,-1,[2,2]]
    center_po = [[3,1],-1,[0,1],-1,-1,[1,1],-1,-1,[2,1]]
    
    left_x = 3
    left_y = 0
    right_x = 3
    right_y = 2
    for n in numbers:
        
        if n in left:
            answer += 'L'
            left_x = left_po[n][0]
            left_y = left_po[n][1]
        elif n in right:
            answer += 'R'
            right_x = right_po[n][0]
            right_y = right_po[n][1]
        else:
            a = center_po[n][0]
            b = center_po[n][1]
            if abs(a-left_x)+abs(b-left_y) > abs(a-right_x)+abs(b-right_y):
                answer += 'R'
                right_x = a
                right_y = b
            elif abs(a-left_x)+abs(b-left_y) < abs(a-right_x)+abs(b-right_y):
                answer += 'L'
                left_x = a
                left_y = b
            else:
                if hand == "right":
                    answer += 'R'
                    right_x = a
                    right_y = b
                else:
                    answer += 'L'
                    left_x = a
                    left_y = b
        # print(left_x,left_y, "..", right_x, right_y)
            
    return answer