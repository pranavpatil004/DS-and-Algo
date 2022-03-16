
def solve(bags, children, candies):
    return sum(candies)%children


T = int(input())
for t in range(T):
    bags, children = map(int, input().split())
    candies = [int(_) for _ in input().split()]
    print('Case #1:', solve(bags, children, candies))


