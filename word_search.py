class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(word, word_index, word_length, board, pos_i, pos_j, l, b):
        	if word_index == word_length:
        		return True
        	
        	if pos_i >= l or pos_i < 0 or pos_j < 0 or pos_j >= b:
        		return False

        	if word[word_index] == board[pos_i][pos_j]:
        		board[pos_i][pos_j] = "-"
        		found = dfs(word, word_index+1, word_length, board, pos_i+1, pos_j, l, b) or \
        				dfs(word, word_index+1, word_length, board, pos_i-1, pos_j, l, b) or \
        				dfs(word, word_index+1, word_length, board, pos_i, pos_j+1, l, b) or \
        				dfs(word, word_index+1, word_length, board, pos_i, pos_j-1, l, b) 
        		board[pos_i][pos_j] = word[word_index]
        		return found
        	return False
        l = len(board)
        b = len(board[0])
        wl = len(word)
        for i in range(l):
        	for j in range(b):
        		if dfs(word, 0, wl, board, i, j, l, b):
        			return True
        return False

# board =[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
board = [["A", "B", "C", "B"]]
s = Solution()
print(s.exist(board, "ABCE"))