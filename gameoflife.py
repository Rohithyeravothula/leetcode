class Solution:
    def gameOfLife(self, board: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        l = len(board)
        b = len(board[0])
        def get_status(i,j,board,l,b):
            children = [(i+1,j), (i-1,j), (i, j+1), (i, j-1), (i+1,j-1), (i-1, j+1), (i+1, j+1), (i-1, j-1)]
            children = [(x,y) for x,y in children if (x>=0 and x<l) and (y>=0 and y<b)]
            s = 0
            for x,y in children:
                if abs(board[x][y]) == 1:
                    s += 1
            return s

        for i in range(l):
            for j in range(b):
                s = get_status(i,j,board,l,b)
                if board[i][j] == 1 and (s<2 or s>3):
                    board[i][j] = -1
                elif board[i][j] == 0 and s==3:
                    board[i][j] = 2 # reproduced
        for i in range(l):
            for j in range(b):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1

