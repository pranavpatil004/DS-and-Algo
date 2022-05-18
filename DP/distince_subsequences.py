class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def numDistinct(self, A, B):
        dp = [[0]*(len(A)+1) for i in range(len(B)+1)]
        for i in range(len(A)+1):
            dp[0][i] = 1
        for row in range(1, len(B)+1):
            for col in range(1, len(A)+1):
                if B[row-1] != A[col-1]:
                    dp[row][col] = dp[row][col-1]
                else:
                    dp[row][col] = dp[row][col-1] + dp[row-1][col-1]
        print(dp)
        return dp[-1][-1]
print(Solution().numDistinct("aaaababbababbaabbaaababaaabbbaaabbb", "bbababa"))
