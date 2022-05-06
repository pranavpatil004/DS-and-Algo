# from copy import deepcopy
# class Solution:

#     def __init__(self):
#         self.ans = []
    
#     def recurse(self, A, row, board, cols, col_set, left_diag_set, right_diag_set):
#         if row == A:
#             for i in range(A):
#                 for j in range(A):
#                     board[i][j] = "Q" if board[i][j] == 1 else "."
#             final = ["".join(_) for _ in board]
#             self.ans.append(final)
#             return
        
#         backup = deepcopy(board)

#         for col in range(cols):
#             new = deepcopy(backup)
#             if row > col:
#                 right_diag = str(row-col) + "0"
#             elif row < col:
#                 right_diag = "0" + str(col-row)
#             else:
#                 right_diag = "00"
#             if col not in col_set and row+col not in left_diag_set and right_diag not in right_diag_set:
#                 col_set.add(col)
#                 left_diag_set.add(row+col)
#                 right_diag_set.add(right_diag)
#                 new[row][col] = 1
#                 self.recurse(A, row+1, new, cols, col_set, left_diag_set, right_diag_set)         
#                 left_diag_set.remove(row+col)
#                 col_set.remove(col)
#                 right_diag_set.remove(right_diag)

#     # @param A : integer
#     # @return a list of list of strings
#     def solveNQueens(self, A):
#         board = [[0]*A for _ in range(A)]
#         self.recurse(A, 0, board, A, set(), set(), set())
#         print(len(self.ans))
#         return self.ans


# print(Solution().solveNQueens(10))


# from copy import deepcopy
# class Solution:

#     def __init__(self):
#         self.ans = []
    
#     def recurse(self, A, row, board, cols, col_set, left_diag_set, right_diag_set):
#         if row == A:
#             for i in range(A):
#                 for j in range(A):
#                     board[i][j] = "Q" if board[i][j] == 1 else "."
#             final = ["".join(_) for _ in board]
#             self.ans.append(final)
#             return
        
#         backup = deepcopy(board)

#         for col in range(cols):
#             new = deepcopy(backup)
#             if col not in col_set and row+col not in left_diag_set and row-col not in right_diag_set:
#                 col_set.add(col)
#                 left_diag_set.add(row+col)
#                 right_diag_set.add(row-col)
#                 new[row][col] = 1
#                 self.recurse(A, row+1, new, cols, col_set, left_diag_set, right_diag_set)         
#                 left_diag_set.remove(row+col)
#                 col_set.remove(col)
#                 right_diag_set.remove(row-col)

#     # @param A : integer
#     # @return a list of list of strings
#     def solveNQueens(self, A):
#         board = [[0]*A for _ in range(A)]
#         self.recurse(A, 0, board, A, set(), set(), set())
#         # print(len(self.ans))
#         return self.ans


# class Solution:
#     # @param A : integer
#     # @return a list of list of strings
#     def solveNQueens(self, A):
#         n=A
#         stack, res = [[(0, i)] for i in range(n)], []
#         print(stack)
#         while stack:
#             board = stack.pop()
#             row = len(board)
#             if row == n:
#                 res.append([''.join('Q' if i == c else '.' for i in range(n))
#                             for r, c in board])
#             for col in range(n):
#                 if all(col != c and abs(row-r) != abs(col-c)for r, c in board):
#                     stack.append(board+[(row, col)])
#         return res

# print(Solution().solveNQueens(10))

A = 7
col = set()
pos_diag = set()
neg_diag = set()

res = []
board = [["."]*A for i in range(A)]

def backtrack(r):
    if r==A:
        copy = ["".join(row) for row in board]
        res.append(copy)
        return
    for c in range(A):
        if c in col or r+c in pos_diag or r-c in neg_diag:
            continue
        col.add(c)
        pos_diag.add(r+c)
        neg_diag.add(r-c)
        board[r][c] = 'Q'
        col.remove(c)
        pos_diag.remove(r+c)
        neg_diag.remove(r-c)
        board[r][c] = '.'


