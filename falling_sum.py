class Solution:
    def minFallingPathSum(self, a: 'List[List[int]]') -> 'int':
    	l = len(a)
    	for i in range(1, l):
    		a[i][0] += min(a[i-1][0], a[i-1][1])
    		a[i][-1] += min(a[i-1][-1], a[i-1][-2])
    		for j in range(1, l-1):
    			a[i][j] += min([a[i-1][j-1], a[i-1][j], a[i-1][j+1]])
    	return min(a[-1])

print(Solution().minFallingPathSum([[1]]))