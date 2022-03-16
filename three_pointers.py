from bisect import bisect_left
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        '''Takes in a number n, returns the square of n'''
        lnA = len(A)
        lnB = len(B)
        lnC = len(C)
        mn = min(lnA, lnB, lnC)
        if lnB == mn:
            A, B = B, A
        elif lnC == mn:
            A, C = C, A
        mn_sm = float('inf')
        for i in range(len(A)):
            pos_b = bisect_left(B, A[i])
            pos_c = bisect_left(C, A[i])
            ele_b = 0
            if pos_b == len(B):
                ele_b = B[pos_b-1]
            elif pos_b > 0:
                ele_b = B[pos_b] if abs(B[pos_b] - A[i]) < abs(B[pos_b-1] - A[i]) else B[pos_b-1]
            else:
                ele_b = B[pos_b]
            
            ele_c = 0
            if pos_c == len(C):
                ele_c = C[pos_c-1]
            elif pos_c > 0:
                ele_c = C[pos_c] if abs(C[pos_c] - A[i]) < abs(C[pos_c-1] - A[i]) else C[pos_c-1]
            else:
                ele_c = C[pos_c]
            
            mn_sm = min(mn_sm, max(abs(A[i]-ele_b), abs(ele_b-ele_c), abs(ele_c-A[i])))

        return mn_sm


Solution().minimize()