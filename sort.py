class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        i = 0
        pos = -1
        while i < len(A):
            print(i, A[i])
            if A[i] == 0:
                if pos == -1:
                    ele = A.pop(i)
                    print('pop ', A)
                    A.insert(0, ele)
                    print(A)
                    i += 1
                else:
                    A[i], A[pos] = A[pos], A[i]
                    i -= 1
                    pos = -1
            elif A[i] == 2:
                pos = i
                i += 1
            elif A[i] == 1 and pos != -1:
                A[i], A[pos] = A[pos], A[i]
                i -= 1
                pos = -1
            else:
                i += 1
        return A
            
A = [0,0,1,2,1,0,0,1,1,1,2,2,2,2,2,1,1,1,1,1,0,0,0,0,1,0,2,0,2,1,2,1]
Solution().sortColors(A)
print(A)
