# # Doesn't work
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def coinchange2(self, A, B):
        A = sorted(A)
        cache = {}
        self.sset = {}
        self.temp = set()
        def recurse(A, B):
            if B == 0:
                return 0
            if B in cache:
                return cache[B]
            cnt = 0
            
            for i in A:
                if i > B:
                    break
                if tuple(sorted([i, B-i])) not in self.temp:
                    if i == B:
                        self.temp.add(tuple(sorted([i, B-i])))
                        cnt += 1
                    else:
                        self.temp.add(tuple(sorted([i, B-i])))
                        cnt += recurse(A, B-i)
                    if B == 4:
                        print(cnt, i, self.temp)
            
            cache[B] = cnt
            # print(B, cache)
            return cnt
        
        return recurse(A, B)
        # print(cache)


        
print(Solution().coinchange2([1,2,3], 5))