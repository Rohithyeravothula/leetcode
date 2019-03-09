from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: 'List[List[str]]') -> 'List[str]':
        adj = defaultdict(list)
        for i,(s,e) in enumerate(tickets):
            adj[s].append((e, i))
        for key in adj:
            adj[key].sort()

        def dfs(node, adj, route, pe, l):
            if len(pe) == l:
                route.append(node)
                return True
            route.append(node)
            for curc,curi in adj[node]:
                if curi not in pe:
                    pe.add(curi)
                    if dfs(curc, adj, route, pe, l):
                        return True
                    pe.remove(curi)
            route.pop()
            return False
            

        route = []
        dfs("JFK", adj, route, set(), len(tickets))
        return route

inp = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
inp = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
inp = [["JFK", "KEN"], ["KEN", "JFK"]]
inp = []
inp = [["JFK", "MN"], ["MN", "TEM"], ["TEM", "JFK"]]
print(Solution().findItinerary(inp))

