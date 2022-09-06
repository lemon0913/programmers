from itertools import combinations
import sys
input = sys.stdin.readline
if __name__ == "__main__":
    n, k = map(int, input().split())
    answer = 0

    base = {'a', 'n', 't', 'i', 'c'}
    remain = {'b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z'}

    words = []
    for i in range(n):
        word = input()
        words.append(word[4:-4])

    
    def countReadableWords(words, learned):
        cnt = 0
        for word in words:
            flag = True
            for w in word:
                # 안배워서 못 읽음
                if not learned[ord(w)] :
                    flag = False
                    break
            if flag:
                cnt += 1
        
        return cnt

    if k < 5:
        print(0)
    else:
        learned = [False]*123
        for x in base:
            learned[ord(x)] = True

        # 남은 알파벳 중에서 k-5개를 선택해본다
        for teach in list(combinations(remain, k-5)):
            for t in teach:
                learned[ord(t)] = True
            
            cnt = countReadableWords(words, learned)

            if cnt > answer:
                answer = cnt
            
            for t in teach:
                learned[ord(t)] = 0
        
        print(answer)