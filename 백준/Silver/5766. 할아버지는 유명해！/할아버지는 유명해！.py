

import sys
input = sys.stdin.readline

while True:

    n,m = map(int, input().split())
    
    if n == 0 and m == 0:
        break

    player = {}

    for _ in range(n):
        tmp = list(map(int, input().split()))
        for t in tmp:
            if t not in player:
                player[t] = 1
            else:
                player[t] += 1
    
    player_idx = sorted(player.items(), key = lambda x:x[0])
    player_cnt = list(sorted(set(player.values())))
    
    sec = player_cnt[-2]
    for i,c in player_idx:
        if c == sec:
            print(i, end = ' ')
    
    print()