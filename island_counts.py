class Solution:
    def numIslands(self, g):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        l = len(g)
        if not g or g==[[]]:
            return 0
        b = len(g[0])
        # hanlde empty case
        
        def get_children(i, j, l, b):
            moves = [(-1, 0), (1, 0), (0, -1), (0,1)]
            children = []
            for x,y in moves:
                ip = i+x
                jp = j+y
                if ip >= 0 and ip<l and jp >=0 and jp<b:
                    children.append((ip, jp))
            return children
        
        def bfs(i,j, g, l, b):
            cur = [(i,j)]
            c = 0
            while cur:
                newcur = []
                for x,y in cur:
                    children = get_children(x,y,l,b)
                    # print(children)
                    for child in children:
                        if g[child[0]][child[1]] == '1':
                            g[child[0]][child[1]] = 2
                            newcur.append(child)
                            c+=1
                cur = newcur
            return c+1
        
        count = 0
        for i in range(l):
            for j in range(b):
                if g[i][j] == '1':
                    g[i][j] = 2
                    bfs(i,j,g,l,b)
                    count += 1
                # print(g)
        return count
                    

inp = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
inp = [['1','1'],['1','1']]
print(Solution().numIslands(inp))