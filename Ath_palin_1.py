from math import ceil
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        init = '1'
        for i in range(A-1):
            init = bin(int(init,2))[2:]
            ln = len(init)
            j = 0
            k=ceil(ln/2)
            for j in reversed(range(0,ln//2)):
                if init[j]=='0' and ln%2==0:
                    init = init[:j]+'1'+''.join(['0']*((k-j-1)*2))+'1'+init[ln-j:]
                    break
                elif init[j]=='0' and ln%2!=0:
                    init = init[:j+1]+'1'+''.join(['0']*(max(0,(k-j-2)*2-1)))+'1'+init[ln-j-1:]
                    break
            if j==0:
                init = bin(int(init, 2)+0b10)
            print(init)
        print(init)

Solution().solve(31)