class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def check_magic(g, x, y):
            nums = set(range(1, 10))
            sums = set()
            for i in range(0, 3):
                c = 0
                for j in range(0, 3):
                    if g[x+i][y+j] in nums:
                        nums.remove(g[x+i][y+j])
                    c += g[x+i][y+j]
                sums.add(c)
                c = 0
                for j in range(0, 3):
                    c += g[x+j][y+i]
                sums.add(c)

            sums.add(g[x][y]+g[x+1][y+1]+g[x+2][y+2])
            sums.add(g[x][y+2]+g[x+1][y+1]+g[x+2][y])

            if not nums and len(sums) == 1:
                return True
            return False
            

        l = len(grid)
        if l == 0:
            return 0
        b = len(grid[0])
        count = 0
        for i in range(0, l-2):
            for j in range(0, b-2):
                if check_magic(grid, i, j):
                    count += 1
        return count



ary = [[1,2,3],[4,5,6], [7,8,90]]
# ary = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
# ary = [[8,1,6], [3,5,7], [4,9,2]]
s = Solution()
print(s.numMagicSquaresInside(ary))
