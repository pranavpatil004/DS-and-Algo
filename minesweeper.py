import random
class Minesweeper:
    
    def __init__(self, n, m):
        self.board = [[0]*n for _ in range(m)]
        self.play_board = [[False]*n for _ in range(m)]
        bomb_nums = int(n*m*0.1)
        while bomb_nums > 0:
            row = random.randint(0,m)
            col = random.randint(0,n)

            if self.board[row-1][col-1] != -1:
                self.board[row-1][col-1] = -1
                bomb_nums -= 1
                left = max(col - 1, 0)
                right = min(col + 1,n)
                top = max(row - 1, 0)
                bottom = min(row + 1, m)

                for i in range(top, bottom):
                    for j in range(left, right):
                        if self.board[i-1][j-1] == -1:
                            continue
                        self.board[i-1][j-1] += 1

    def play(self, row, col):
        if self.board[row][col] == -1:
            for pos_i, ele_i in enumerate(self.board):
                for pos_j, ele_j in enumerate(ele_i):
                    if ele_j == -1:
                        self.play_board[pos_i][pos_j] = True
            return self.play_board
        
        if self.board[row][col] != 0:
            self.play_board[row][col] = True
            return self.play_board
        else:
            self.open_empty_cell(row, col)
            return self.play_board
    def open_empty_cell(self, row, col):

        if self.board[row][col] == -1:
            return

        if self.board[row][col] != 0:
            self.play_board[row][col] = True
            return
        
        if self.board[row][col] == 0:
            left = max(col - 1, 0)
            right = min(col + 1,len(self.board[0]))
            top = max(row - 1, 0)
            bottom = min(row + 1, len(self.board))

            for i in range(top, bottom):
                for j in range(left, right):
                    if self.board[i][j] == -1 or self.play_board[i][j]:
                        continue
                    self.play_board[i][j] = True
                    self.open_empty_cell(i, j)
        

        
    
mn = Minesweeper(10,10)

print(mn.board)

mn.open_empty_cell(1, 2)

print(mn.board)
print(mn.play_board)