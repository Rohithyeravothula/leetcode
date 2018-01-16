class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0, 9, 3):
        	for j in range(0, 9, 3):
        		visited = {}
        		for ri in range(i, i+3):
        			for rj in range(j, j+3):
        				if board[ri][rj] in visited:
        					return False
        				elif board[ri][rj] != ".":
        					visited.add(board[ri][rj])
        for i in range(0, 9):
        	visited = {}
        	for j in range(0, 9):
        		if board[i][j] in visited:
        			return False
        		elif board[i][j] != ".":
        			visited.add(board[i][j])

        for j in range(0, 9):
        	visited = {}
        	for i in range(0, 9):
        		if board[i][j] in visited:
        			return False
        		elif board[i][j] != ".":
        			visited.add(board[i][j])
        return True
