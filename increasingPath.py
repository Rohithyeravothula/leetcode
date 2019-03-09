class Solution:
    def longestIncreasingPath(self, matrix: 'List[List[int]]') -> 'int':
        if not matrix:
            return 0
        l = len(matrix)
        b = len(matrix[0])
        def get_children(i, j, l, b):
            ans = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            ans = [(x,y) for (x,y) in ans if (x>=0 and x<l) and (y>=0 and y<b)]
            return [(x,y) for (x,y) in ans if matrix[i][j] < matrix[x][y]]

        def dfs(i,j,pe, seen,l,b):
            if (i,j) in seen:
                return seen[(i,j)]
            pe.add((i,j))
            count = 1
            for x,y in get_children(i,j,l,b):
                if (x,y) not in pe:
                    count = max(count, 1+dfs(x,y,pe,seen,l,b))
            pe.remove((i,j))
            seen[(i,j)] = count
            return count

        seen = {}
        ans = 0
        for i in range(l):
            for j in range(b):
                ans = max(ans, dfs(i,j,set(),seen,l,b))
        return ans

inp = [[9,9,4],[6,6,8],[2,1,1]] 
inp = [[3,4,5],[3,2,6],[2,2,1]]
inp = [[1,2,3,4,5,6,7]]
inp = [[5,4,3,2,1]]
inp = [[1], [2], [3]]
inp = [[3]]
print(Solution().longestIncreasingPath(inp))


