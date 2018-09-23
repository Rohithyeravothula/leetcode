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
        n = 58
        m = [[0]*n for _ in range(n)]
        for i in range(l):
            for j in range(b):
                m[i+1][j+1] = grid[i][j]
        area = 0
        for i in range(1, n-1):
            for j in range(1, n-1):
                area += max(0, m[i][j] - m[i-1][j])
                area += max(0, m[i][j] - m[i+1][j])
                area += max(0, m[i][j] - m[i][j-1])
                area += max(0, m[i][j] - m[i][j+1])
                if m[i][j] != 0:
                    area += 2
        return area

        

s = Solution()
# inp = [[2]]
# inp = []
# inp = [[1,2],[3,4]]
# inp = [[1,0],[0,2]]
# inp = [[1,1,1],[1,0,1],[1,1,1]]
# inp = [[2,2,2],[2,1,2],[2,2,2]]
inp = [[1], [2,3]]
print(s.surfaceArea(inp))