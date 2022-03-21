class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        ln = len(A)
        for i in range(ln):
            for j in range(i, ln-1):
                # print(i, j)
                try:
                    temp = A[i][j]
                    A[i][j] = A[ln-j-1][i]
                    A[ln-j-1][i] = A[ln-i-1][ln-j-1]
                    A[ln-i-1][ln-j-1] = A[ln-(ln-j-1)-1][ln-i-1]
                    A[ln-(ln-j-1)-1][ln-i-1] = temp
                except Exception:
                    print('Error ', i, j)
        
        return A


Solution().rotate([[1,2], [3,4]])