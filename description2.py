class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def mark(a, c, x, y, l, b, visited):
            if x>=l or x<0 or y>=b or y<0 or visited[x][y] != 0 or a[x][y] == 0:
                return None
            visited[x][y] = c
            mark(a, c, x+1, y, l, b, visited)
            mark(a, c, x-1, y, l, b, visited)
            mark(a, c, x, y+1, l, b, visited)
            mark(a, c, x, y-1, l, b, visited)

        l=len(grid)
        if l == 0:
            return 0
        b=len(grid[0])
        visited=[]
        for i in range(0, l):
            visited.append([0]*b)
        
        for i in range(0, l):
            for j in range(0, b):
                grid[i][j] = int(grid[i][j])

        count = 2
        for i in range(0, l):
            for j in range(0, b):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    mark(grid, count, i, j, l, b, visited)
                    count+=1
        print(visited)
        return count-1

a=[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
s=Solution()
s.numIslands(a)