class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        def get_status(board, i, j):

            if board[i][j] == 1 and c==3:
                return 1
            if c<2 or c>3:
                return 0
            if c==2 or c==3:
                return 1
            
                        
        
        def recr(board, i, j, m, n):
            if i<0 or i>=m:
                return None
            if j<0 or j>=n:
                return None

            cur = get_status(board, i, j)
            # print(i, j, cur)
            recr(board, i+1, j, m, n)
            recr(board, i, j+1, m, n)
            recr(board, i+1, j+1, m, n)
            board[i][j] = cur
            
        m=len(board)
        n=len(board[1])
        recr(board, 0, 0, m, n)
        print(board)

s=Solution()
a=[[1,0], [0,1]]
# a=[[1,1,0, 0, 0], [0, 1,1,1,1], [1,0,0,1,1], [1,1,1,1,1]]
s.gameOfLife(a)



# if i == 0 and j == 0:
# c=board[i+1][j] + board[i][j+1] + board[i+1][j+1]
# elif i == 0 and 
# c=board[i][j-1] + board[i][j+1] + board[i+1][j] + board[i+1][j+1]+ board[i+1][j-1]
# else:
# c=board[i][j-1] + board[i][j+1] + board[i+1][j] + board[i-1][j] + board[i+1][j+1] + board[i-1][j+1] + board[i+1][j-1]