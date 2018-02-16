class Solution:
    def slidingPuzzle(self, initial_board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        def swaps(initial, position, curboard):
        	ans = []
        	curlist = list(curboard)
        	for p in position:
        		boardlist = curlist[:]
        		boardlist[initial], boardlist[p] = boardlist[p], boardlist[initial]
        		ans.append(tuple(boardlist))
        	return ans


        def get_children(curboard):
        	swapmap = {0:[1,3], 1:[0,2,4], 2:[1,5], 3:[0,4], 4:[1,3,5], 5:[2,4]}
        	boardlist = list(curboard)
        	for i in range(0, 6):
        		if boardlist[i] == 0:
        			return swaps(i, swapmap[i], curboard)
        
        def check_goal(curboard):
        	if curboard == (1,2,3,4,5,0):
        		return True
        	return False


        board = (initial_board[0][0],initial_board[0][1],initial_board[0][2],initial_board[1][0],initial_board[1][1],initial_board[1][2])
        # print(board)
        if check_goal(board):
        	return 0


        initial = [board]
        visited = set()
        count = 1
        while count < 100000:
        	# print(count)
        	next_states = []
        	for state in initial:
        		children = get_children(state)
        		for child in children:
        			if child not in visited:
        				if check_goal(child):
        					return count
        				else:
        					next_states.append(child)
        					visited.add(child)
        	count += 1
        	initial = next_states
        return -1


bb= [[3,2,4],[1,5,0]] 
s=Solution()
print(s.slidingPuzzle(bb))