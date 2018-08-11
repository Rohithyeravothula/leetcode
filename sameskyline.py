class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        l = len(grid)
        b = len(grid[0])
        if b == 0:
            return 0
        row_max = [0]*l
        col_max = [0]*b
        for i in range(0, l):
            row_max[i] = max(grid[i])
        # print(row_max)
        for j in range(0, b):
            col_max[j] = grid[0][j]
            for i in range(0, l):
                col_max[j] = max(col_max[j], grid[i][j])
        # print(col_max)
        count = 0
        for i in range(0, l):
            for j in range(0, b):
                count += max(0, min(row_max[i], col_max[j]) - grid[i][j])
        return count



# g = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
g = [[1]]
s=Solution()
print(s.maxIncreaseKeepingSkyline(g))
