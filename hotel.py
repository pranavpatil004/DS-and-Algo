class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive = [ 1, 2, 3, 4 ], depart=[ 10, 2, 6, 14 ], K=2):
        #depart = sorted(depart)
        #print(depart)
        j = 0
        for i in range(len(arrive)):
            K -= 1
            j = 0
            while j < i:
                if j < len(depart):
                    if depart[j] < arrive[i]:
                        depart.remove(depart[j])
                        K += 1
                    j += 1
                else:
                    break
            if K < 0:
                return False
        else:
            return True
    
print(Solution().hotel())