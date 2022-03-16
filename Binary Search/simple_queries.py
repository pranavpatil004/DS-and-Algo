from math import floor, sqrt
from random import randrange
import time
import numpy as np


from collections import defaultdict
import bisect

def getDivsProd(n):
    mod = 1000000007
    p = 1
    for i in range(1, int(n**0.5 + 1)):
        if n%i==0:
            if n/i==i: p = (p*i)%mod
            else:
                p = (p*i)%mod
                p = (p*(n/i))%mod
    return int(p%mod)

def getFrequency(A):
    N = len(A)
    L = [1]*N
    R = [1]*N
    S = []
    top = -1
    for i in range(N):
        while(top >= 0 and A[S[top]] <= A[i]):
            S.pop()
            top -= 1
        if (top >= 0):
            L[i] = i - S[top]
        else:
            L[i] = i + 1
        S.append(i)
        top += 1
    S = []
    top = -1
    for i in range(N-1, -1, -1):
        while(top >= 0 and A[S[top]] < A[i]):
            S.pop()
            top -= 1
        if (top >= 0):
            R[i] = S[top] - i
        else:
            R[i] = N - i
        S.append(i)
        top += 1
    for i in range(N):
        L[i] *= R[i]
    return L
    

class Solution1:
    def solve(self, A, B):
        N = len(A)
        freq = getFrequency(A)
        for i in range(N):
            A[i] = getDivsProd(A[i])
        keys = []
        values = []
        prev = 0
        for i in sorted(zip(A, freq), reverse = True):
            keys.append(i[0])
            prev += i[1]
            values.append(prev)
        res = []
        for i in B:
            res.append(keys[bisect.bisect_left(values,i)])
        return res

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def divisor(self, n):
        n_sqrt = floor(sqrt(n))
        ml = 1
        for i in range(1, n_sqrt+1):
            if n%i == 0:
                ml = (ml * i)%(10**9+7)
                if n//i != i:
                    ml = (ml * (n//i))%(10**9+7)
                ml = ml%(10**9+7)
        return ml%(10**9+7)
    
    def getFrequency(self, A):
        stk = []
        L = [0]*len(A)
        for pos, ele in enumerate(A):
            if pos == 0:
                L[pos] = 1
                stk.append(pos)
            else:
                if ele >= A[stk[-1]]:
                    while stk and A[stk[-1]] <= ele:
                        stk.pop()
                    #L[pos] = pos-stk[-1]
                
                if stk and ele < A[stk[-1]]:
                    for i in reversed(range(1, len(stk))):
                        L[stk[i]] += (stk[i]-stk[i-1])
                    L[stk[0]] += (stk[0] + 1)
                    L[pos] = (pos-stk[-1])
                    stk.append(pos)
                elif len(stk) == 0:
                    stk.append(pos)
                    L[pos] = (pos + 1)
            #print(pos, ele, L, stk)
        #print(L)
        return L

    def solve(self, A, B):
        freq = self.getFrequency(A) 
        divsr = []
        #print(freq)
        for pos, ele in enumerate(A):
            d = self.divisor(ele)
            divsr.extend([d]*freq[pos])
        divsr = sorted(divsr, reverse=True)
        # print(divsr, len(divsr))
        # print(divsr[0], divsr[51])
        return [divsr[_-1] for _ in B]
'''calculate time take by the program'''

A = list(np.random.randint(10, size=10**4))

start_time = time.time()

print("A creation --- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("B creation --- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(Solution().solve(A, B))
print("A removed old method --- %s seconds ---" % (time.time() - start_time))
print('after A: ', len(A))

start_time = time.time()
print(Solution1().solve(A, B))
print("B removed new method --- %s seconds ---" % (time.time() - start_time))
print('after B: ', len(B))