w1 = input()
w2 = input()
w3 = input()
w4 = input()
w5 = input()

l1 = len(w1)
l2 = len(w2)
l3 = len(w3)
l4 = len(w4)
l5 = len(w5)

m = max(l1,l2,l3,l4,l5)
w1 += ' '*(m-l1)
w2 += ' '*(m-l2)
w3 += ' '*(m-l3)
w4 += ' '*(m-l4)
w5 += ' '*(m-l5)

result = ''
for i in range(m):
    result += w1[i] + w2[i] + w3[i] + w4[i] + w5[i]

print(result.replace(' ',''))