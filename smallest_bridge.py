class Solution:
    def shortestBridge(self, a):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        def get_children(i,j,n):
            children = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            return [(x,y) for x,y in children if x>=0 and x<n and y>=0 and y<n]

        def change_an_island(i,j,n,a):
            cur = [(i,j)]
            while cur:
                newcur = []
                for ci,cj in cur:
                    children = get_children(ci,cj,n)
                    for chi, chj in children:
                        if a[chi][chj] == 1:
                            a[chi][chj] = 2
                            newcur.append((chi, chj))
                cur = newcur


        n = len(a)
        changed = False
        for i in range(n):
            for j in range(n):
                if a[i][j] == 1:
                    a[i][j] = 2
                    change_an_island(i,j,n,a)
                    changed = True
                    break
            if changed:
                break

        # for row in a:
        #   print(row)

        
        first = [(i,j) for i in range(n) for j in range(n) if a[i][j]==1]
        second = [(i,j) for i in range(n) for j in range(n) if a[i][j]==2]
        count = 0
        while first or second:
            newfirst = []
            for fi, fj in first:
                children = get_children(fi, fj,n)
                for ci,cj in children:
                    if a[ci][cj] == 2:
                        return count
                    elif a[ci][cj] == 0:
                        a[ci][cj] = 1
                        newfirst.append((ci, cj))
            first = newfirst
            count += 1
            newsecond = []
            for si, sj in second:
                children = get_children(si, sj, n)
                for ci, cj in children:
                    if a[ci][cj] == 1:
                        return count
                    elif a[ci][cj] == 0:
                        a[ci][cj] = 2
                        newsecond.append((ci, cj))
            second = newsecond
            count += 1
            # print(first, second)
        return count




# inp = [[1,1,1], [1,0,0], [0,1,1]]
inp = [[0,1],[1,0]]
inp = [[0,1,0],[0,0,0],[0,0,1]]
inp = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
inp = [[1]]
print(Solution().shortestBridge(inp))



        