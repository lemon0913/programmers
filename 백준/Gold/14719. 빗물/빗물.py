if __name__ == "__main__":
    H, W = map(int, input().split())
    heights = list(map(int, input().split()))

    answer = 0
    for i in range(1, W-1):
        left_max = max(heights[:i])
        right_max = max(heights[i+1:])

        compare = min(left_max, right_max)

        if heights[i] < compare:
            answer += (compare-heights[i])
    
    print(answer)
