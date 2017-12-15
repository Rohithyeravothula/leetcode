from collections import deque
from graph import *

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        queue = deque([node])
        created = {}
        created[node] = UndirectedGraphNode(node.label)
        visited = set()
        while queue:
            cur = queue.popleft()
            if cur not in visited:
                clone = created[cur]
                for c in cur.neighbors:
                    if c not in created:
                        created[c] = UndirectedGraphNode(c.label)
                    clone.neighbors.append(created[c])
                    if c not in visited:
                        queue.append(c)
                visited.add(cur)
            # print_graph(created[node;])
        return created[node]


s=Solution()
print_graph(test)
g = s.cloneGraph(test)
print_graph(g)