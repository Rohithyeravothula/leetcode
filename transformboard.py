class Solution:
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        l = len(board)
        def get_board(curboardstring):
        	curboard = []
        	for i in range(0, l*l, l):
        		print(curboardstring[i:i+l])
        		curboard.append(list(curboardstring[i:i+l]))
        	
        	curcolboard = []
        	for i in range(0, l):
        		for j in range(0, l):

        	return curboard, curcolboard

        def get_children(curboardstring):
        	children = []
        	curboard, curcolboard = get_board[curboardstring]
        	for i in range(0, l):
        		for j in range(0, l):
        			piece = curboard[:]
        			piece[i], piece[j] = piece[j], piece[j]
        			children.append(get_str(piece))

        	

        def get_str(curboard):
        	return "".join(list(map(lambda x: "".join(list(map(lambda y: str(y), x))), curboard)))
        get_children(get_str(board))
s=Solution()
s.movesToChessboard([[0, 1], [1, 0]])