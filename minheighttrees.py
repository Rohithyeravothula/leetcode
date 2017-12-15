class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def get_children(root, adjMatrix):
        	children = []
        	for i in range(0, n):
        		if adjMatrix[i][root] == 1 and i != root:
        			children.append(i)

        	return children

        visited = [0]*n
        adj = [[0]*n for _ in range(0, n)]
       	for e in edges:
       		adj[e[0]][e[1]] = 1
       		adj[e[1]][e[0]] = 1
       		degrees[]

       	heights = [float("inf")]*n
       	for i in range(0,n):
       		if sum(adj[i]) == 1:
       			heights[i] = 0

       	

