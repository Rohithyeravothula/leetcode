class Solution:
    def updateMatrix(self, matrix: 'List[List[int]]') -> 'List[List[int]]':
    	l = len(matrix)
    	b = len(matrix[0])
    	ans = [[float('inf')]*b for _ in range(l)]
    	for i in range(l):
    		for j in range(b):
    			if matrix[i][j] == 0:
    				ans[i][j] = 0
    	for j in range(1, b):
    		ans[0][j] = min(ans[0][j], 1+ans[0][j-1])

    	for i in range(1, l):
    		ans[i][0] = min(ans[i][0], 1+ans[i-1][0])
    		for j in range(1, b-1):
    			ans[i][j] = min(ans[i][j], 1+min([ans[i][j-1], ans[i-1][j]]))
    		if b>1:
	    		ans[i][-1] = min(ans[i][-1], 1+min([ans[i][-2], ans[i-1][-1]]))

    	for j in range(b-2, -1, -1):
    		ans[l-1][j] = min(ans[l-1][j], 1+ans[l-1][j+1])

    	for i in range(l-2, -1, -1):
    		ans[i][-1] = min(ans[i][-1], 1+ans[i+1][-1])
    		for j in range(b-2, -1, -1):
    			ans[i][j] = min(ans[i][j], 1+min([ans[i][j+1], ans[i+1][j]]))
    		if b>1:
	    		ans[i][0] = min(ans[i][0], 1+min([ans[i][1], ans[i+1][0]]))
    	return ans


inp = []
inp = [[0,0,0],[0,1,0],[1,1,1]]
inp = [[0,0,0],[0,1,0],[0,0,0]]
inp = [[0,1,1],[1,1,1],[1,1,1]]
inp = [[1,0,1,1,1]]
inp = [[1],[1],[0]]
print(Solution().updateMatrix(inp))