import sys
from itertools import permutations 
if __name__ == "__main__":
    n = int(input())
    k = int(input())
    card = [0]*n
    for i in range(n):
        card[i] = sys.stdin.readline().replace('\n', '')
    
    result = list(permutations(card, k))
    for i in range(len(result)):
        result[i] = ''.join(result[i])
    
    print(len(set(result)))