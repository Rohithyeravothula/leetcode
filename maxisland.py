class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def get_children(x,y,l,b):
            ans = []
            if x+1 < l:
                ans.append([x+1,y])
            if x-1 >= 0:
                ans.append([x-1, y])
            if y+1 < b:
                ans.append([x, y+1])
            if y-1 >= 0:
                ans.append([x,y-1])
            return ans

        l = len(grid)
        if l == 0:
            return 0
        b = len(grid[0])
        visited = [[0]*b for _ in range(0, l)]
        max_ans = 0
        for i in range(0, l):
            for j in range(0, b):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    stk = [[i,j]]
                    count = 1
                    while stk:
                        # print(stk, count)
                        cur = stk.pop()
                        children = get_children(cur[0], cur[1], l, b)
                        visited[cur[0]][cur[1]] = 1
                        for child in children:
                            if visited[child[0]][child[1]]==0 and grid[child[0]][child[1]]==1:
                                count += 1
                                stk.append(child)
                                visited[child[0]][child[1]] = 1
                    max_ans = max(max_ans, count)
        return max_ans

gg=[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
s=Solution()
print(s.maxAreaOfIsland(gg))
