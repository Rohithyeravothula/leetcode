class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix:
        	return True
        l = len(matrix)
        b = len(matrix[0])
        for x in range(l):
        	i,j = x,0
        	exp = matrix[i][j]
        	while i<l and j<b:
        		if matrix[i][j] != exp:
        			return False
        		j+=1
        		i+=1

        for y in range(b):
        	i,j=0,y
        	exp = matrix[i][j]
        	while i<l and j<b:
        		if matrix[i][j] != exp:
        			return False
        		i+=1
        		j+=1
        return True

inp = [[1,2],[3,2]]
inp = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
inp = [[1,2,3,4,5], [1,1,2,3,5]]
inp = [[]]
print(Solution().isToeplitzMatrix(inp))