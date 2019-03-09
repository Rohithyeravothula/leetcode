from collections import defaultdict
class Solution:
    def removeStones(self, stones: 'List[List[int]]') -> 'int':
        rows = defaultdict(list)
        cols = defaultdict(list)
        for x,y in stones:
            rows[x].append([x,y])
            cols[y].append([x,y])
        def dfs(node, rows, cols, pe, te):
            if node in te:
                return 
            x,y = node
            pe.add(node)
            for cx, cy in rows[x] + cols[y]:
                if (cx, cy) not in pe and (cx, cy) not in te:
                    dfs((cx, cy), rows, cols, pe, te)
            pe.remove((x,y))
            te.add((x,y))

        count = 0 
        te = set()
        for x,y in stones:
            if (x,y) not in te:
                dfs((x,y), rows, cols, set(), te)
                count += 1
        return len(stones) - count



inp = [[1,2],[1,3],[3,3],[3,1],[2,1],[1,0]]
inp = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
inp = [[0,0],[0,2],[1,1],[2,0],[2,2]]
inp = [[0,0]]
print(Solution().removeStones(inp))