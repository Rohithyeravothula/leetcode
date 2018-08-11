class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjlist = [[] for _ in range(numCourses)]
        degree_count = [0]*numCourses
        for i,j in prerequisites:
            degree_count[i] += 1
            adjlist[j].append(i)

        # visited: not fully explored
        # explored: fully explored

        def topo_order(cur, adj, visited, explored, order):
            # print(cur, visited, explored)
            if cur in explored:
                return []
            for child in adj[cur]:
                if child in visited:
                    return False
                elif child not in explored:
                    visited.add(child)
                    order_exists = topo_order(child, adj, visited, explored, order)
                    if order_exists == False:
                        return order_exists
                    visited.remove(child)
                    explored.add(child)
            order.append(cur)


        topo_sort = []
        outside_visited = set()
        outside_explored = set()
        for i in range(numCourses):
            if i not in outside_explored and degree_count[i] == 0:
                order_exists = topo_order(i, adjlist, outside_visited, outside_explored, topo_sort)
                if order_exists == False:
                    return []
        if len(topo_sort) == numCourses:
            return topo_sort[::-1]
        return []


nc = 2
info = [[1,0]]
s = Solution()
print(s.findOrder(nc, info))



