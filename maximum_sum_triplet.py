class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A = [16542, 4834, 31116, 4640, 29659, 22705, 9931, 13978, 2307, 31674, 22387, 5022, 28746, 26925, 19073, 6271, 5830, 26778, 15574]):
        lt = sorted([(i,j) for i, j in enumerate(A)], key=lambda x: x[1])
        mx = 0
        for i in range(0, len(lt)):
            mx1, mx2 = 0, 0
            for j in range(i+1, len(lt)):
                if lt[j][0] > lt[i][0]:
                    if lt[j][0] > mx1 >= mx2:
                        mx2 = mx1
                        mx1 = j
            if mx1 > 0 and mx2 > 0:
                mx = max(mx, lt[i][1] + lt[mx1][1] + lt[mx2][1])
        return mx

print(Solution().solve())