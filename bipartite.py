class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        if not graph:
        	return True
        visited = {}
        l = len(graph)
        for i in range(0, l):
        	if i in visited:
        		continue
	        visited[i] = 1
        	color = -1
	        cur = [i]
	        while cur:
	        	next_cur = []
	        	for i in cur:
	        		for j in graph[i]:
	        			if j not in visited:
	        				visited[j] = color
	        				next_cur.append(j)
	        			elif visited[j] != color:
	        				return False
	        	color *= -1
	        	cur = next_cur
        return True

# gph = [[1,2,3], [0,2], [0,1,3], [0,2]]
gph = [[], [2,3], [1,3]]
s = Solution()
print(s.isBipartite(gph))


