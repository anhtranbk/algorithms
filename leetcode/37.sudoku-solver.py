#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
from typing import List

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_int = [None]*9
        for i in range(0, 9):
            board_int[i] = [int(e) if e != '.' else 0 for e in board[i]]

        self.solveSudoku0(board=board_int)

        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    board[i][j] = str(board_int[i][j])

    def solveSudoku1(self, board: List[List[int]]) -> None:
        flags = [None]*9
        counts = [None]*9
        for i in range(0, 9):
            flags[i] = [0]*9
            counts[i] = [9]*9
            for j in range(0, 9):
                if board[i][j] != 0:
                    counts[i][j] = 0
                else:
                    for k in range(0, 9):
                        if board[i][k] != 0 and k != j:
                            flags[i][j] |= 1 << board[i][k]

                        if board[k][j] != 0 and k != i:
                            flags[i][j] |= 1 << board[k][j]

                    r = i // 3 * 3
                    c = j // 3 * 3
                    for u in range(r, r + 3):
                        for v in range(c, c + 3):
                            if u != i and v != j and board[u][v] != 0:
                                flags[i][j] |= 1 << board[u][v]
        
        self.backtracking(board, flags)

    def backtracking(self, board, flags):
        # backtracking
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != 0: continue
                for k in range(1, 10):
                    t = 1 << k 
                    if board[i][j] & t == 0:
                        flags[i][j] |= t
                        self.backtracking(board, flags)
                        flags[i][j] ^= t

    def solveSudoku0(self, board: List[List[int]]) -> None:
        flags = [None]*9
        counts = [None]*9
        for i in range(0, 9):
            flags[i] = [0]*9
            counts[i] = [9]*9
            for j in range(0, 9):
                if board[i][j] != 0:
                    counts[i][j] = 0
                else:
                    for k in range(0, 9):
                        if board[i][k] != 0 and k != j:
                            self.updateState(board, flags, counts, i, j, board[i][k])

                        if board[k][j] != 0 and k != i:
                            self.updateState(board, flags, counts, i, j, board[k][j])

                    r = i // 3 * 3
                    c = j // 3 * 3
                    for u in range(r, r + 3):
                        for v in range(c, c + 3):
                            if u != i and v != j and board[u][v] != 0:
                                self.updateState(board, flags, counts, i, j, board[u][v])

        # self.printBoard(board=self.convert2StrBoard(board=flags))
        # self.printBoard(board=self.convert2StrBoard(board=counts))

        # self.printBoard(board=self.convert2StrBoard(board=board))

        while True:
            cnt = 0
            for i in range(0, 9):
                for j in range(0, 9):
                    if counts[i][j] == 1:
                        for t in range(1, 10):
                            if flags[i][j] & (1 << t) == 0:
                                self.putValue(board, flags, counts, i, j, t)
                        cnt += 1
            if cnt == 0:
                break

        self.printBoard(board=self.convert2StrBoard(board=board))

        while True:
            success = 0
            for t in range(1, 10):
                for i in range(0, 9):
                    cnt = 9
                    k = -1
                    for j in range(0, 9):
                        if board[i][j] != 0 or flags[i][j] & (1 << t) != 0:
                            cnt -= 1
                        else:
                            k = j
                    if cnt == 1:
                        self.putValue(board, flags, counts, i, k, t)
                        success += 1

            for t in range(1, 10):
                for j in range(0, 9):
                    cnt = 9
                    k = -1
                    for i in range(0, 9):
                        if board[i][j] != 0 or flags[i][j] & (1 << t) != 0:
                            cnt -= 1
                        else:
                            k = i
                    if cnt == 1:
                        self.putValue(board, flags, counts, k, j, t)
                        success += 1

            for t in range(1, 10):
                for i in range (0, 3, 3):
                    for j in range(0, 3, 3):
                        cnt = 9
                        ux, vx = -1, -1
                        for u in range(i, i + 3):
                            for v in range(j, j + 3):
                                if board[u][v] != 0 or flags[u][v] & (1 << t) != 0:
                                    cnt -= 1
                                else:
                                    ux, vx = u, v
                        if cnt == 1:
                            self.putValue(board, flags, counts, ux, vx, t)
                            success += 1
                
            if success == 0:
                break

        self.printBoard(board=self.convert2StrBoard(board=board))
        # self.printBoard(board=self.convert2StrBoard(board=counts))

        # backtracking for remain empty cell, last strategy


    # O(9*9*9)
    def putValue(self, board, flags, counts, i, j, t):
        for k in range(0, 9):
            if k != j:
                self.updateState(board, flags, counts, i, k, t)

            if k != i:
                self.updateState(board, flags, counts, k, j, t)

        r = i // 3 * 3
        c = j // 3 * 3
        for u in range(r, r + 3):
            for v in range(c, c + 3):
                if u != i and v != j:
                    self.updateState(board, flags, counts, u, v, t)

        board[i][j] = t
        flags[i][j] = 1023
        counts[i][j] = 0

    def updateState(self, board, flags, counts, i, j, t):
        t = 1 << t
        if flags[i][j] & t == 0 and counts[i][j] > 0:
            counts[i][j] -= 1
        flags[i][j] |= t

    def convert2StrBoard(self, board: List[List[int]]) -> List[List[str]]:
        board_str = [None]*9
        for i, row in enumerate(board):
            board_str[i] = [None]*9
            for j, cell in enumerate(row):
                board_str[i][j] = str(cell) if cell else '.'
        return board_str
                

    def printBoard(self, board: List[List[str]]):
        print()
        for row in board:
            print(' '.join(row))


# @lc code=end
if __name__ == '__main__':
    inp = [
        '53..7....',
        '6..195...',
        '.98....6.',
        '8...6...3',
        '4..8.3..1',
        '7...2...6',
        '.6....28.',
        '...419..5',
        '....8..79'
    ]
    inp = [
        [".",".","9","7","4","8",".",".","."],
        ["7",".",".",".",".",".",".",".","."],
        [".","2",".","1",".","9",".",".","."],
        [".",".","7",".",".",".","2","4","."],
        [".","6","4",".","1",".","5","9","."],
        [".","9","8",".",".",".","3",".","."],
        [".",".",".","8",".","3",".","2","."],
        [".",".",".",".",".",".",".",".","6"],
        [".",".",".","2","7","5","9",".","."]
    ]
    board = [None]*9
    for i in range(0, 9):
        if isinstance(inp[i], str):
            board[i] = list(inp[i])
        else:
            board[i] = inp[i]

    s = Solution()
    
    s.solveSudoku(board=board)

    # s.printBoard(board=board)
        

