class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A = [ 1, 1, 1, 1 ], B = 3):
        curr_max, lone, max_d = -1, 0, 0
        blbs = 0
        for i in range(len(A)):
            if A[i] == 1:
                if (i-curr_max) > B-1:
                    if curr_max == -1 or i - curr_max 
                    blbs += 1
                    lone = i
                    curr_max = i
                    max_d= 0
                else:
                    lone = i
            else:
                max_d += 1
                if (max_d >= B-1 and curr_max == -1):
                    return -1
                if max_d >= 2*(B-1) and lone == curr_max:
                    return -1
        if max_d >= B-1 and A[-1] == 0:
            return -1
        else:
            return blbs
            
print(Solution().solve())