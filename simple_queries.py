from math import sqrt, floor
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def divisor(self, n):
        n_sqrt = floor(sqrt(n))
        #print(n, n_sqrt)
        #print(n_sqrt)
        ml = 1
        for i in range(1, n_sqrt+1):
            if n%i == 0:
                ml = (ml * i)%(10**9+7)
                if n//i != i:
                    ml = (ml * (n//i))%(10**9+7)
                ml = ml%(10**9+7)
        #print(n, ml)
        return ml%(10**9+7)

    def solve(self, A, B):
        A = sorted(A, reverse=True)
        G = []
        for i in range(len(A)):
            print(i, A[i])
            d = self.divisor(A[i])
            print([d])
            G.extend([d]*(len(A)-i))
        print(G)
        M = sorted(G,reverse=True)
        print(M)
        return [G[i] if 0<=i<len(G) else 1 for i in B]
        
        
        
Solution().solve([39, 99, 70, 24, 49, 13, 86, 43, 88, 74, 45, 92, 72, 71, 90, 32, 19, 76, 84, 46, 63, 15, 87, 1, 39, 58, 17, 65, 99, 43, 83, 29, 64, 67, 100, 14, 17, 100, 81, 26, 45, 40, 95, 94, 86, 2, 89, 57, 52, 91, 45], [1221, 360, 459, 651, 958, 584, 345, 181, 536, 116, 1310, 403, 669, 1044, 1281, 711, 222, 280, 1255, 257, 811, 409, 698, 74, 838])