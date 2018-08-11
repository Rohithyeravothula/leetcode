class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i, j, il, jl, g, v):
        	if i >= il or i < 0 or j >= jl or j < 0 or v[i][j] == 1 or g[i][j] == "0":
        		return None
        	v[i][j] = 1
        	dfs(i+1, j, il, jl, g, v)
        	dfs(i-1, j, il, jl, g, v)
        	dfs(i, j+1, il, jl, g, v)
        	dfs(i, j-1, il, jl, g, v)
        if not grid:
        	return 0
        l = len(grid)
        b = len(grid[0])
        visited = [[0]*b for _ in range(l)]
        count = 0
        for i in range(l):
        	for j in range(b):
        		if visited[i][j] == 0 and grid[i][j] == "1":
        			dfs(i, j, l, b, grid, visited)
        			count += 1
        return count

inp = []
s = Solution()
print(s.numIslands(inp))