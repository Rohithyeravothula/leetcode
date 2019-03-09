class Solution:
    def orangesRotting(self, grid: 'List[List[int]]') -> 'int':

        def forward(ans, l, b):
            for i in range(1, b):
                if grid[0][i] != 0:
                    ans[0][i] = min(ans[0][i], 1+ans[0][i-1])

            
            for i in range(1, l):
                if grid[i][0] != 0:
                    ans[i][0] = min(ans[i][0], 1+ans[i-1][0])
                for j in range(1, b):
                    if grid[i][j] != 0:
                        ans[i][j] = min(ans[i][j], 1+min(ans[i][j-1], ans[i-1][j]))

        def backward(ans, l, b):
            for i in range(b-2, -1, -1):
                if grid[l-1][i] != 0:
                    ans[l-1][i] = min(ans[l-1][i],1+ans[l-1][i+1])

            for i in range(l-2, -1, -1):
                if grid[i][-1] != 0:
                    ans[i][-1] = min(ans[i][-1], 1+ans[i+1][-1])
                for j in range(b-2, -1, -1):
                    if grid[i][j] != 0:
                        ans[i][j] = min(ans[i][j], 1+min(ans[i][j+1], ans[i+1][j]))

        if not grid:
            return 0
        l = len(grid)
        b = len(grid[0])
        ans = [[float('inf')]*b for _ in range(l)]

        for i in range(l):
            for j in range(b):
                if grid[i][j] == 2:
                    ans[i][j] = 0
        for _ in range(5):
            forward(ans, l, b)
            backward(ans, l, b)
            
        result = 0
        # for row in grid:
        #   print(row)
        # print()
        # for row in ans:
        #   print(row)

        for i in range(l):
            for j in range(b):
                if grid[i][j] == 1:
                    result = max(result, ans[i][j])
        return result if result != float('inf') else -1


inp = [[2,1,1],[1,1,0],[0,1,1]]
inp = [[2,1,1],[0,1,1],[1,0,1]]
inp = [[0,2]]
inp = [[2],[1],[2]]
inp = []
inp = [[]]
inp = [[1,2,1,1,1],[1,0,2,1,2]]
inp = [[1,2,0,0],[0,2,1,2]]
print(Solution().orangesRotting(inp))
