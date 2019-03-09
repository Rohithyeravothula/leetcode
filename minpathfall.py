class Solution:
    def minFallingPathSum(self, a):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if a==[] or a==[[]]:
        	return 0
        l = len(a)
        opt = list(a[0])
        for i in range(1, l):
        	cur = [0]*l
        	cur[0] = a[i][0] + min([opt[0], opt[1]])
        	for j in range(1, l-1):
        		cur[j] = a[i][j] + min([opt[j-1], opt[j], opt[j+1]])
        	cur[-1] = a[i][-1] + min(opt[-1], opt[-2])
        	opt = cur
        return min(opt)

# inp = [[1,2,3],[4,5,6],[7,8,9]]
inp = [[1,2], [3,4]]
inp = [[1]]
inp = [[]]
print(Solution().minFallingPathSum(inp))
