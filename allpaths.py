class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def get_children(adj, parent):
        	children = []
        	for i in range(0, LENGTH):
        		if adj[parent][i] == 1:
        			children.append(i)
        	return children

        LENGTH = len(graph)
        adj = [[0] * LENGTH for _ in range(0, LENGTH)]
        for i in range(0, LENGTH):
        	for j in graph[i]:
        		adj[i][j] = 1

        queue = [[0]]
        paths = []
        while queue:
        	cur = []
        	for path in queue:
        		children = get_children(adj, path[-1])
        		for child in children:
        			if child == LENGTH - 1:
        				paths.append(path + [child])
        			else:
        				cur.append(path+[child])
        	queue = cur
        return paths

# gph = [[1,2], [3], [3], []]
# gph = [[1,4], [2], [5], [2,5], [3], []]
gph = []
s=Solution()
print(s.allPathsSourceTarget(gph))