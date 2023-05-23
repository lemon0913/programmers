# 투포인터로 푼거 아닌거 같음...

# n, x = map(int, input().split())
# visit = list(map(int, input().split()))

# maxV = 0
# c = 0
# for i in range(n-x+1):
#   s = sum(visit[i:i+x])
#   if s > maxV:
#     c = 1
#     maxV = s
#   elif s == maxV:
#     c += 1


# if maxV == 0:
#   print('SAD')
# else:
#   print(maxV)
#   print(c)

#################################
# 슬라이딩 윈도우로 다시 풀어보기
n,x = map(int, input().split())
visit = list(map(int, input().split()))

s = sum(visit[0:x])
c = 1
maxV = s

for i in range(1,n-x+1):
  s -= visit[i-1]
  s += visit[i+x-1]

  if s > maxV:
    c = 1
    maxV = s
  elif s == maxV:
    c += 1
    
if maxV == 0:
  print('SAD')
else:
  print(maxV)
  print(c)