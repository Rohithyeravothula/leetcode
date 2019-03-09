class Solution:
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        l = len(graph)
        opt = [[-1]*l for _ in range(l)]
        for i in range(l):
        	opt[0][i] = 1

        
        for i in range(1, l):
        	for j in range(2, l):
        		opt


inp = [[], [], []]
inp = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
print(Solution().catMouseGame(inp))
        				