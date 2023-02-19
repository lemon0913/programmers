
# 처음에 어떻게 풀어야 하는건지 감도 안왔는데
# 이거 보니 풀이는 생각보다 간단했다....
# https://tmdrl5779.tistory.com/128

##################################################3
# 이렇게 하면 안되는데 왜 안되는건지 모르겠네....

# duck = input()
# l = len(duck)
# visited = [False]*(l)
# cnt = 0

# # 녹음한 소리가 올바르지 않은 경우
# # - 문자열을 모두 방문을 하지 않았을때
# # - 오리가 0마리 일때
# # - 문자열의 길이가 5의 배수가 아닐때
# if l % 5 != 0:
#     print(-1)
#     exit()


# def solve(start):
#     global cnt
#     pre = ''
#     k_cnt = 0

#     for i in range(start,l):
#         if duck[i] == 'q' and not visited[i]:
#             visited[i] = True
#             pre = 'q'
#             print(i)
#             continue
        
#         elif duck[i] == 'u' and not visited[i] and pre == 'q':
#             visited[i] = True
#             pre = 'u'
#             print(i)
#             continue

#         elif duck[i] == 'a' and not visited[i] and pre == 'u':
#             visited[i] = True
#             pre = 'a'
#             print(i)
#             continue

#         elif duck[i] == 'c' and not visited[i] and pre == 'a':
#             visited[i] = True
#             pre = 'c'
#             print(i)
#             continue

#         elif duck[i] == 'k' and not visited[i] and pre == 'c' and k_cnt == 0:
#             visited[i] = True
#             pre = 'k'
#             cnt += 1
#             k_cnt += 1
#             print(i)
#             continue

#         elif duck[i] == 'k' and not visited[i] and pre == 'c' and k_cnt > 0:
#             visited[i] = True
#             pre = 'k'
#             k_cnt += 1
#             print(i)
#             continue




# for i in range(l):
#     if duck[i] == 'q' and not visited[i]:
#         solve(i)

# print(visited)
        


# if False in visited or cnt == 0:
#     print(-1)
# else:
#     print(cnt)


#################################################################3


duck = input()
visited = [False] * len(duck)
cnt = 0

if len(duck) % 5 != 0:
    print(-1)
    exit()


def solve(start):
    global cnt
    prev_s = None
    k_cnt = 0
    q_cnt = 0
    for i in range(start, len(duck)):
        if not visited[i] and duck[i] == 'q' and q_cnt == 0:
            visited[i] = True
            prev_s = duck[i]
            q_cnt += 1
            continue
        if not visited[i] and duck[i] == 'q' and prev_s == 'k':
            visited[i] = True
            prev_s = duck[i]
            continue


        if not visited[i] and duck[i] == 'u' and prev_s == 'q':
            visited[i] = True
            prev_s = duck[i]
            continue

        if not visited[i] and duck[i] == 'a' and prev_s == 'u':
            visited[i] = True
            prev_s = duck[i]
            continue

        if not visited[i] and duck[i] == 'c' and prev_s == 'a':
            visited[i] = True
            prev_s = duck[i]
            continue

        if not visited[i] and duck[i] == 'k' and prev_s == 'c' and k_cnt == 0:
            visited[i] = True
            prev_s = duck[i]
            cnt += 1
            k_cnt += 1
            continue
        if not visited[i] and duck[i] == 'k' and prev_s == 'c' and k_cnt > 0:
            visited[i] = True
            prev_s = duck[i]
            continue


for i in range(len(duck)):
    if duck[i] == 'q' and not visited[i]:
        solve(i)

if False in visited or cnt == 0:
    print(-1)
else:
    print(cnt)