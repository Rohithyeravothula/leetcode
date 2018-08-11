
class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        def get_children(adj, root, n):
            children = []
            for i in range(0, n):
                if adj[root][i] and root!=i:
                    children.append(i)
            return children


        l = len(graph)
        adj = [[0]*l for _ in range(0, l)]
        for e in range(0, l):
            edges = graph[e]
            for j in edges:
                adj[e][j] = 1
                adj[j][e] = 1
        red = set()
        black = set()
        queue = []
        while True:
            for i in range(0, l):
                if i not in red and i not in black:
                    queue = [i]
                    black.add(i)
                    break
            if not queue:
                break
            color = "R"
            while queue:
                next_children = []
                # print(queue, red, black, color)
                for node in queue:
                    children = get_children(adj, node, l)
                    if color == "R":
                        for child in children:
                            if child in black:
                                return False
                            if child not in red:
                                red.add(child)
                                next_children.append(child)
                    else:
                        for child in children:
                            if child in red:
                                return False
                            if child not in black:
                                black.add(child)
                                next_children.append(child)
                if color == "R":
                    color = "B"
                else:
                    color = "R"
                queue = next_children
        return True


graphdesc = []
s=Solution()
print(s.isBipartite(graphdesc))