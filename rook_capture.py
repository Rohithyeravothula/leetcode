from typing import List
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        pos = None
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    pos = (i, j)
                    break
            if pos:
                break
        count = 0
        x,y = pos
        bk = {'p', 'B'}
        while x>=0:
            if board[x][y] == 'p':
                count += 1
            if board[x][y] in bk:
                break
            x-=1

        x,y = pos
        while x<8:
            if board[x][y] == 'p':
                count += 1
            if board[x][y] in bk:
                break
            x+=1

        x,y = pos
        while y<8:
            if board[x][y] == 'p':
                count += 1
            if board[x][y] in bk:
                break
            y+=1

        x,y = pos
        while y>=0:
            if board[x][y] == 'p':
                count += 1
            if board[x][y] in bk:
                break
            y-=1
        return count

inp = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
inp = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
inp = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]

print(Solution().numRookCaptures(inp))
