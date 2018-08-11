class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        #n is number of nodes
        adj = {}
        for (i,j),v in zip(equations, values):
            if i in adj:
                adj[i].append((j, v))
            else:
                adj[i] = [(j, v)]
            
            if j in adj:
                adj[j].append((i, 1/v))
            else:
                adj[j] = [(i, 1/v)]

        def bfs(start, end, computed):
            seen = set()
            cur = [start]
            found = False
            while cur and not found:
                new_cur = []
                for node in cur:
                    if node in adj:
                        for (node_end, val) in adj[node]:
                            computed[(node, node_end)] = val
                            computed[(start, node_end)] = computed[(start, node)] * val
                            if node_end not in seen:
                                new_cur.append(node_end)

                            if node_end == end:
                                found = True
                        seen.add(node)
                cur = new_cur

        ans = []
        computed = {}
        for i, j in queries:
            if i not in adj or j not in adj:
                ans.append(-1.0)
            elif i==j:
                ans.append(1.0)
            else:
                computed[(i,i)] = 1.0
                computed[(j,j)] = 1.0
                if (i, j) in computed:
                    ans.append(computed[(i, j)])
                else:
                    bfs(i, j, computed)
                    if (i, j) in computed:
                        ans.append(computed[(i, j)])
                    else:
                        ans.append(-1.0)
        return ans


# equations = [ ["a", "b"], ["b", "c"] ]
equations = [("m", "n")]
# values = [2.0, 3.0]
values = [1.2]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
s = Solution()
print(s.calcEquation(equations, values, queries))
