class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        ans = 0
        l = len(grid)
        b = len(grid[0])
        for i in range(l):
            j = 0
            while j<b:
                found = False
                while j<b and grid[i][j] == 1:
                    found = True
                    j+=1
                if found: ans += 2
                j+=1
        j=0
        while j<b:
            i=0
            while i<l:
                found = False
                while i<l and grid[i][j] == 1:
                    found = True
                    i+=1
                if found: ans += 2
                i+=1
            j+=1
        return ans
s = Solution()
inp = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
inp = []
inp = [[0,1,1,0],[0,1,0,0],[0,1,0,0],[0,0,0,0]]
print(s.islandPerimeter(inp))