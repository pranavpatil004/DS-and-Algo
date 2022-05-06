# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def is_valid(self, A):
        mn_val = mx_val = A.val
        res = True
        if A.left:
            left_res, left_mn_val, left_mx_val = self.is_valid(A.left)
            if not left_res or left_mx_val >= A.val:
                return False, mn_val, mx_val
            mn_val = min(left_mn_val, mn_val)
            mx_val = max(left_mx_val, mx_val)
        
        if A.right:
            right_res, right_mn_val, right_mx_val = self.is_valid(A.right)
            if not right_res or right_mn_val<A.val:
                return False, mn_val, mx_val
            mn_val = min(right_mn_val, mn_val)
            mx_val = max(right_mx_val, mx_val)

        return True, mn_val, mx_val

    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        res, mn, mx = self.is_valid(A)
        return 1 if res else 0


#        3
#     2      4
# 1      3

        
