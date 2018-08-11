class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
        	return None
        l = len(board)
        b = len(board[0])
        def toY(i,j, il, jl, b):
        	if i<0 or j<0 or i>=il or j>=jl or b[i][j] != "O":
        		return None
        	b[i][j] = "Y"
        	toY(i+1, j, il, jl, b)
        	toY(i-1, j, il, jl, b)
        	toY(i, j+1, il, jl, b)
        	toY(i, j-1, il, jl, b)

        for i in range(0, l):
        	toY(i, 0, l, b, board)
        	toY(i, b-1, l, b, board)
        for j in range(0, b):
        	toY(0, j, l, b, board)
        	toY(l-1, j, l, b, board)

        for i in range(0, l):
        	for j in range(0, b):
        		if board[i][j] == "O":
        			board[i][j] = "X"
        		elif board[i][j] == "Y":
        			board[i][j] = "O"


# inp = [["X", "X", "X"], ["X", "O", "X"], ["X", "O", "O"]]
inp = []
s = Solution()
s.solve(inp)
print(inp)

