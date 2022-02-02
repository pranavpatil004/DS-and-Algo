class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A = [1,2,3,-4,100]):
        max_sum = 0
        pos_left, pos_right = 0, 0
        sum_so_far = 0
        new_left, new_right = 0 ,0
        for i in range(len(A)):
            if A[i]<0:
                sum_so_far = 0
                new_left = i+1
                new_right = 0
            else:
                sum_so_far += A[i]
                new_right = i
                if sum_so_far > max_sum:
                    max_sum = sum_so_far
                    pos_left, pos_right = new_left, new_right
                elif sum_so_far == max_sum and (pos_right-pos_left)<(new_right-new_left):
                    pos_left, pos_right = new_left , new_right
                # elif sum_so_far == max_sum and (pos_right-pos_left)==(new_right-new_left):
                #     continue
        if pos_left == 0 and pos_right == 0 and A[0] < 0:
            return []
        else:
             return A[pos_left:pos_right+1]

print(Solution().maxset())