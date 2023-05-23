
n,m = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

# lenA = n-1
# lenB = m-1
pointA = 0
pointB = 0
result = []

while True:
	if pointA == n and pointB == m:
		break
		
	if pointA == n:
		result.append(arrB[pointB])
		pointB += 1
	
	elif pointB == m:
		result.append(arrA[pointA])
		pointA += 1
	
	else:
		if arrA[pointA] < arrB[pointB]:
			result.append(arrA[pointA])
			pointA += 1
		else:
			result.append(arrB[pointB])
			pointB += 1

print(' '.join(map(str, result)))


# n,m = map(int, input().split())
# arrA = list(map(int, input().split()))
# arrB = list(map(int, input().split()))
# result = arrA + arrB
# result.sort()
# print(' '.join(map(str, result)))