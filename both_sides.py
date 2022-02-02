class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A=[ -533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35 ], B=48):
        ln = len(A)
        l,r = 0, ln-1
        final_sum = 0
        for i in range (0, B):
            if A[l] + final_sum > A[r] + final_sum:
                final_sum += A[l]
                l += 1
            else:
                final_sum += A[r]
                r -= 1
        return final_sum

print(Solution().solve())