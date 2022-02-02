class Solution:
    # @param A : integer
    # @return an integer
    def isPalin(self, s):
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True

    def solve(self, A):
        i = 1
        cnt = 0
        while True:
            s = i + i - 1
            if self.isPalin(bin(s)[2:]):
                cnt += 1
            #print(s, cnt)
            if cnt == A:
                return s
            i += 1
        
print(Solution().solve(20000))