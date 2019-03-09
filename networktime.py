class Solution:
    def networkDelayTime(self, times: 'List[List[int]]', n: 'int', k: 'int') -> 'int':
        if n==1:
            return 0
        seen = {i:float('inf') for i in range(n)}
        adj = [[float('inf')]*n for _ in range(n)]
        for u,w,t in times:
            adj[u-1][w-1] = t
        def get_children(u):
            children = []
            for j in range(n):
                if adj[u][j]!=float('inf'):
                    children.append(j)
            return children
        cur = [(k-1,0)]
        seen[k-1] = 0
        count = 0
        while cur and count <= n:
            nxt = []
            for (x,t) in cur:
                for y in get_children(x):
                    if seen[y] > (t+adj[x][y]):
                        seen[y] = t+adj[x][y]
                        nxt.append((y, t+adj[x][y]))
            cur = nxt
            count += 1
        # seen = [val if val != float("inf") else -1 for val in seen.values()]
        ans = max(seen.values())
        return ans if ans != float("inf") else -1

inp = []
inp = [[2,1,1],[2,3,1],[3,4,1],[1,4,0]]
inp = [[1,2,1],[2,1,1]]
n = 2
k = 1
print(Solution().networkDelayTime(inp, n, k))
