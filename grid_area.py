class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area = 0
        l = len(grid)
        for i in range(0, l):
            m = grid[i][0]
            for j in range(0, l):
                if grid[i][j]:
                    area += 1
                m = max(m, grid[i][j])
            area += m
        for j in range(0, l):
            m = grid[0][j]
            for i in range(0, l):
                m = max(m, grid[i][j])
            area += m
        return area

inp = [[1]]
s = Solution()
print(s.projectionArea(inp))
