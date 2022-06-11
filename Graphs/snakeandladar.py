from collections import deque
class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def snakeLadder(self, A, B):
        q = deque()
        A = sorted(A)
        B = sorted(B)
        laddars, snakes = {a[0]: a[1] for a in A}, {b[0]:b[1] for b in B}
        q.append((1, 0))
        is_visited = set()
        min_ans = 100
        is_found = False
        while q:
            ele, height = q.popleft()
            if ele not in is_visited:
                if ele == 100:
                    is_found = True
                    min_ans = min(height, min_ans)
                if (ele + 6) >= 100 and ele not in snakes:
                    is_found = True
                    min_ans = min(height+1, min_ans)
                elif ele in laddars:
                    q.append((laddars[ele], height))
                    # is_visited.add(ele)
                elif ele in snakes:
                    q.append((snakes[ele], height))
                    is_visited.add(ele)
                else:
                    lad = 0
                    while lad < len(A) and A[lad][0] <= (ele + 6):
                        if ele < A[lad][0] <= ele + 6:
                            q.append((A[lad][0], height+1))
                            # A.pop(0)
                        lad += 1
                    snk = 0
                    while snk < len(B) and B[snk][0] <= (ele+6):
                        if ele < B[snk][0] <= ele+6:
                            q.append((B[snk][0], height+1))
                            # B.pop(0)
                        snk += 1
                    q.append((ele+6, height+1))
            # print(q)
        return min_ans if is_found else -1

A = [
  [3, 5],
  [7, 8],
  [44, 56],
  [36, 54],
  [88, 91],
  [77, 83],
  [2, 4],
  [9, 99],
  [45, 78],
  [31, 75]
]
B = [
  [10, 6],
  [95, 90],
  [96, 30],
  [97, 52],
  [98, 86]
]

# A = [
#   [3, 54],
#   [37, 100]
# ]
# B = [
#   [56, 33]
# ]



print(Solution().snakeLadder(A, B))

