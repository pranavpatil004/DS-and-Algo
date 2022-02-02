class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        dct = {}
        count = 0
        i,j = 0, 0
        while i < len(A) and j < len(A):
            if A[j] in dct.keys():
                dct[A[j]] = dct[A[j]] + 1
            else:
                dct[A[j]] =  1
            keys = dct.keys()
            if len(keys) < B:
                j += 1
            if len(keys) > B:
                dct[A[j]] = dct[A[j]] - 1
                dct[A[i]] = dct[A[i]] - 1
                if dct[A[i]] == 0:
                    del dct[A[i]]
                i += 1
                if i>=len(A) :
                    break
                continue

            if len(keys) == B:
                count += sum(dct.values())-B+1
                j += 1
        return count


print(Solution().solve([1, 1, 1, 1, 2, 1, 1, 1, 1, 10], 2))

#1 1 1 1 2 1 1 1 1 10

#1+6-2+1+7-2+1+8-2+1+9-2+1+5-2+1

#2-2+1+3-2+1+4-2+1+1