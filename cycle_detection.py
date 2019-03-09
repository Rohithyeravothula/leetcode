class Solution:
    def eventualSafeNodes(self, graph: 'List[List[int]]') -> 'List[int]':
        def dfs(node, pe, te, seen):
            if node in pe or node in seen:
                return True
            if node in te:
                return False

            pe.add(node)
            result = False
            for child in graph[node]:
                result = result or dfs(child, pe, te, seen)
            pe.remove(node)
            te.add(node)
            if result:
                seen[node] = result
            return result
        ans = []
        l = len(graph)
        te = set()
        seen = {}
        for i in range(l):
            if not dfs(i, set(), te, seen):
                ans.append(i)
        return ans

inp = [[0],[],[]]
inp = [[1,2],[2,3],[5],[0],[5],[],[]]
inp = [[1],[2],[]]
print(Solution().eventualSafeNodes(inp))
