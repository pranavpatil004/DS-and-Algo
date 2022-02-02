import math
from collections import Counter
class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A='cdfacbeb'):
        chars = sorted([char for char in A])
        dict_val = Counter(A)
        print(dict_val)
        def rec(a, chars):
            if len(chars) == 1:
                return 1
            ind = chars.index(a[0])
            ln = len(chars)
            sm = 0
            st = set(chars[:ind])
            for i in st:
                temp = math.factorial(ln-1)
                #print('before division ', sm)
                for key, val in dict_val.items():
                    #print('a ', a[0], 'key ', key, 'val ', val)
                    if key == i:
                        temp //= math.factorial(val-1)
                    else:
                        temp //= math.factorial(val)
                sm += temp
                #print('after division ', sm)
            if dict_val[a[0]] == 1:
                del dict_val[a[0]]
            else:
                dict_val[a[0]] -= 1
            chars.pop(ind)
            a = a.replace(a[0], '', 1)
            #print(chars)
            #print(a)
            return (sm + rec(a, chars))% 1000003
        return rec(A, chars)

print(Solution().findRank())
#abbccdef - abbcdef - abbcef - bbce - eb
#cdfacbeb - dfacbeb - facbeb - cbeb - eb

#7!/2!2! + 7!/2! ++  6!/2! + 6! + 6!/2! ++ 5!/2! + 5! + 5!/2! + 5!/2! ++ 3! ++  1! + 1


#5528