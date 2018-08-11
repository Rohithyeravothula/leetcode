class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        def get_children(adj, root, n):
            children = []
            for i in range(0, n):
                if adj[i][root] and root!=i:
                    children.append(i)
            return children

        adj = [[0]*n for _ in range(0, n)]
        for (cursrc, curdst, price) in flights:
            adj[cursrc][curdst] = price

        # for o in adj:
        #     print(o)


        opt = [float("inf")]*n
        opt[src] = 0
        for i in range(0, n):
            if adj[src][i] != 0:
                print(src, i, adj[src][i])
                opt[i] = adj[src][i]
        # print(opt)
        for i in range(0, K):
            cur = [float("inf")]*n
            for j in range(0, n):
                children = get_children(adj, j, n)
                for c in children:
                    cur[j] = min(cur[j], opt[c]+adj[c][j])
                cur[j] = min(cur[j], opt[j])
            opt = cur
            # print(opt)
        if opt[dst] == float("inf"):
            return -1
        else:
            return opt[dst]


In = 5
Iedges = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
Isrc = 2
Idst = 1
Ik = 1
s=Solution()
print(s.findCheapestPrice(In, Iedges, Isrc, Idst, Ik))
