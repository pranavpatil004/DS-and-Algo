class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        mid_array = [[0]*(len(A)-B+1) for _ in range(len(A))]
        for row in range(len(mid_array)):
            for col in range(len(mid_array[row])):
                mid_array[row][col] = sum(A[row][col:col+B])
        max_sum = -float('inf')
        
        for row in range(len(mid_array)-B+1):
            for col in range(len(mid_array[row])):
                max_sum = max(max_sum, sum([mid_array[_][col] for _ in range(row, row+B)]))
            
        
        return max_sum
        
        
        # ln = len(A)
        # C = [[0]*(ln-B+1) for i in range(ln)]
        # for j in range(ln):
        #     for i in range(ln-B+1):
        #         C[j][i] = sum([A[j][k] for k in range(i, i+B)])
        # max_a = -float('inf')
        # for j in range(len(C)-B+1):
        #     for i in range(len(C[0])):
        #         sm = sum([C[k][i] for k in range(j, j+B)])
        #         max_a = max(max_a, sm)
        # return max_a 
        
