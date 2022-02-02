class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A = 4):
        final = [[0 for x in range(A)] for y in range(A)] 
        nta = 0
        final[0][0] = nta
        print(final)
        i = j = 0
        i_max = j_max = A
        i_min = 1
        j_min = 0
        is_complete = False
        while not is_complete:
            if nta == A**2:
                is_complete = True
                break
            for j in range (j_min, j_max):
                nta += 1
                print('Inside j positive', nta)
                final[i][j] = nta
                print(final)
            for i in range(i_min, i_max):
                nta += 1
                final[i][j] = nta
            j_max -= 1
            for j in reversed(range(j_min, j_max)):
                nta += 1
                final[i][j] = nta
            
            i_max -= 1
            for i in reversed(range(i_min, i_max)):
                nta += 1
                final[i][j] = nta
            i_min += 1
            j_min += 1
        return final


Solution().generateMatrix()