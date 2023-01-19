# dp 유형인가 싶었지만 그리디였다...ㅎ
# 먼저 빨리 끝나는 회의 순서대로 정렬을 하기...빨리 끝날수록 뒤에서 고려해볼 회의가 많으니까!
# 그 다음에 시작하는 시간 순서대로 정렬하기

n = int(input())

time = []
for _ in range(n):
    time.append(list(map(int, input().split())))

time.sort(key = lambda x:(x[1], x[0]))

cnt = 1
end = time[0][1]
for i in range(1,n):
    if time[i][0] >= end:
        cnt += 1
        end = time[i][1]

print(cnt)