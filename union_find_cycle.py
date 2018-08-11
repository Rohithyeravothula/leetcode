class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        info = [-1]*(1+n)
        def find(i, a):
        	if a[i] == -1:
        		return i
        	root_i = find(a[i], a)
        	a[i] = root_i
        	return root_i

        def union(i, j, a):
        	root_i = find(i, a)
        	root_j = find(j, a)
        	if root_i == root_j:
        		return False
        	else:
        		a[root_i] = root_j
        	return True

        for u, v in edges:
        	if not union(u, v, info):
        		return [u, v]

egs = [[1,2], [2,3], [1,3]]
s = Solution()
print(s.findRedundantConnection(egs))

