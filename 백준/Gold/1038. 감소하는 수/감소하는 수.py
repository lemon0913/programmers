from itertools import combinations
if __name__ == "__main__":

    N = int(input())

    nums = []
    arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(1,11):
        for c in combinations(arr, i):
            c = list(c)
            c.sort(reverse = True)
            nums.append(int(''.join(c)))
    
    nums.sort()

    # if N > len(nums):
    #     print(-1)
    # else:
    #     print(nums[N])
    try:
        print(nums[N])
    except:
        print(-1)
