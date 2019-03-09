class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def get_children(i, j, l, b):
        	c = [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]
        	children = []
        	for ci, cj in c:
        		if ci >= 0 and ci < l and cj >=0 and cj<b:
        			children.append((ci, cj))
        	return children

        def dfs(i, j, pe, m):
        	# print(i, j, pe)
        	l = len(m)
        	b = len(m[0])
        	pe.add((i, j))
        	longest = 0
        	children_explored = 0
        	for ci, cj in get_children(i, j, l, b):
        		if (ci, cj) not in pe and m[ci][cj] != float("inf") and m[ci][cj] > m[i][j]:
        			longest = max(longest, dfs(ci, cj, pe, m))
        			children_explored += 1
        	pe.remove((i, j))
        	if children_explored == 3:
	        	m[i][j] = float("inf")
        	return 1+longest

        maxpath = 0
        l = len(matrix)
        if not matrix:
        	return 0
        b = len(matrix[0])
        pe = set()
        for i in range(l):
        	for j in range(b):
        		if matrix[i][j] != float("inf"):
        			# print(matrix[i][j], maxpath)
        			maxpath = max(maxpath, dfs(i, j, pe, matrix))
        return maxpath

matrix = [[9,9,4], [6,6,8]]
matrix = [[]]
matrix = [[4,3,2,9]]
matrix = []
matrix = [[3,2,1]]
matrix = [[9,9,4],[6,6,8],[2,1,1]]
matrix = [[1,2,3]]
matrix = [[]]
matrix = [[3,4,5],[3,2,6],[2,2,1]] 
print(Solution().longestIncreasingPath(matrix))
print(matrix)
        