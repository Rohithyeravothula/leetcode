class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        l=len(board)
        b=len(board[0])
        i = 0
        j = 0
        count = 0
        while i<l and j<b:
        	local = 0
        	bs = 0
        	for r in range(0, b):
        		if a[i][r] == '-' and bs == 1:
        			bs = 0
        		elif a[i][r] == 'X' and bs == 0:
        			local += 1
        			bs = 1
        	bs = 0
        	for r in range(0, l):
        		if a[r][i] == '-' and bs == 1:
        			bs = 0
        		elif a[r][i] == 'X' and bs == 0:
        			local += 1
        			bs = 1
        	count += local
        	i+=1
        	j+=1
        print(count)


a = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
s = Solution()
s.countBattleships(a)
