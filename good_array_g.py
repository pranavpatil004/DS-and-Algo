class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        dict = {}
        ans = 0
        pos = 0
        for i in range(len(A)):
            if A[i] in dict:
                dict[A[i]] += 1
                if len(dict.keys())==B:
                   ans += sum(dict.values())-B+1
            else:
                if len(dict.keys())<B:
                    dict[A[i]] = 1
                elif len(dict.keys())==B:
                    while len(dict.keys())>=B:
                        dict[A[pos]] -= 1
                        if dict[A[pos]]==0:
                            del dict[A[pos]]
                        pos += 1
                    dict[A[i]]=1
                if len(dict.keys())==B:
                    ans += sum(dict.values())-B+1
            print(dict)
            print(ans)
        return ans

print(Solution().solve([1, 1, 1, 1, 2, 1, 1, 1, 1, 10], 2))