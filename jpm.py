from functools import reduce


def solve(num):
    cnt = 1
    temp = num
    ans = 0
    while temp > 0:
        t = temp%10
        to_add = t if cnt%2 else t*2
        ans += reduce(lambda x,y: int(x)+int(y), list(str(to_add)), 0)
        cnt += 1
        temp //= 10
    return ans

print(solve(6789))