from random import randrange
import time
import numpy as np

class Solution:
    def removeElement(self, A, B):        
        i = 0
        while i<len(A):
            if A[i] == B:
                A.pop(i)
            else:
                i += 1
        return len(A)
    
    def removeElementNew(self, A, B):
        #print(A, B)
        current = 0
        for i in range(len(A)):
            if A[i] != B:
                A[current] = A[i]
                current += 1
        A[:] = A[:current]
        return len(A)

#A = [randrange(1,10) for _ in range(10**10)]
A = list(np.random.randint(10, size=10**8))

start_time = time.time()

print("A creation --- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
B = [char for char in A]
print("B creation --- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
Solution().removeElement(A, 6)
print("A removed old method --- %s seconds ---" % (time.time() - start_time))
print('after A: ', len(A))

start_time = time.time()
Solution().removeElementNew(B, 6)
print("B removed new method --- %s seconds ---" % (time.time() - start_time))
print('after B: ', len(B))