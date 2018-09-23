class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
        	return 0
        l = len(grid)
        b = len(grid[0])
        area = 0
        for row in grid:
        	area += 2*max(row)

        c = 0
        for j in range(b):
        	curmax = -1
        	for i in range(l):
        		curmax = max(curmax, grid[i][j])
        		if grid[i][j] != 0:
        			c+=1
        	area += 2*curmax

        area += 2*c
        

s = Solution()
# inp = [[2]]
# inp = []
# inp = [[1,2],[3,4]]
# inp = [[1,0],[0,2]]
inp = [[1,1,1],[1,0,1],[1,1,1]]
print(s.surfaceArea(inp))