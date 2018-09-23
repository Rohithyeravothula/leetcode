class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def get_children(grid, i, j, l, b):
        	children = []
        	if (i+1) < l and grid[i+1][j] == 1:
        		grid[i+1][j] = 0
        		children.append((i+1, j))
        	if (i-1) >= 0 and grid[i-1][j] == 1:
        		grid[i-1][j] = 0
        		children.append((i-1, j))
        	if (j+1) < b and grid[i][j+1] == 1:
        		grid[i][j+1] = 0
        		children.append((i, j+1))

        	if (j-1) >= 0 and grid[i][j-1] == 1:
        		grid[i][j-1] = 0
        		children.append((i, j-1))

        	return children


        def bfs(grid, i, j, l, b):
        	cur = [(i, j)]
        	grid[i][j] = 0 # set the island visited
        	counter = 1
        	while cur:
        		updated = []
        		for (i, j) in cur:
        			valid_children = get_children(grid, i, j, l, b)
        			updated.extend(valid_children)
        		counter += len(updated)
        		cur = updated
        	return counter


        def dfs_count(grid, i, j, l, b):
        	if i<0 or i>=l or j<0 or j>=b or grid[i][j] == 0:
        		return 0
        	grid[i][j] = 0
        	return 1+dfs_count(grid, i+1, j, l, b)+dfs_count(grid, i-1, j, l, b) + \
        	dfs_count(grid, i, j+1, l, b) + dfs_count(grid, i, j-1, l, b)




        if not grid:
        	return 0
        l = len(grid)
        b = len(grid[0])

        max_area = 0

        for i in range(l):
        	for j in range(b):
        		if grid[i][j] == 1:
        			max_area = max(max_area, dfs_count(grid, i, j, l, b))
        return max_area


ild = [[1,0],[0,1]]
s = Solution()
print(s.maxAreaOfIsland(ild))
