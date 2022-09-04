import math
if __name__ == "__main__":
    x, y = map(int, input().split())
    print(math.gcd(x,y))
    print(math.lcm(x,y))