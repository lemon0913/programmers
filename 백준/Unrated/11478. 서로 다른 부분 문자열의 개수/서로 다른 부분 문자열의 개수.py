result = set()
s = input()
for i in range(1,len(s)+1):
  for j in range(len(s)-i+1):
    result.add(s[j:j+i])
print(len(result))