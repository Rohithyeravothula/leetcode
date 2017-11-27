class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        ng = []
        for i in range(0, m):
        	ng.append([float("inf")]*n)

        ng[0][0] = grid[0][0]

        for i in range(1, n):
        	ng[0][i] = ng[0][i-1] + grid[0][i]
        
        for i in range(1, m):
        	ng[i][0] = ng[i-1][0] + grid[i][0]

        for i in range(1, m):
        	for j in range(1, n):
        		ng[i][j] = min(ng[i-1][j], ng[i][j-1])+grid[i][j]

        return ng[m-1][n-1]
