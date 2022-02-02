class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A = [ 5, 17, 12, 3]):
        ce = co = pe = po = cnt = 0
        for i in range(0, len(A)):
            if i%2 == 0:
                ce += A[i]
            else:
                co += A[i]
        
        for i in range(0, len(A)):
            n = A[i]
            if i%2 == 0:
                # even number removal
                ne = ce - n
                no = co
                no, ne = ne + pe, co + po
                if no == ne:
                    cnt += 1
                ce, co = ce - n, co
                pe += n
            else:
                # odd number removal
                no = co - n
                ne = ce
                ne, no = no + pe, ne + po
                if no == ne:
                    cnt += 1
                ce, co = ce, co - n
                po += n
        print(cnt)
        return cnt

Solution().solve()