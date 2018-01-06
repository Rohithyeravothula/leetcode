class Solution:
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def find(root, ary):
        	if ary[root] == -1:
        		return root
        	k = find(ary[root], ary)
        	ary[root] = k
        	return k

        def union(left, right, ary):
        	pleft = find(left, ary)
        	pright = find(right, ary)
        	if pleft == pright:
        		return False
        	ary[pleft] = pright
        	return True


        l = len(edges)
        ary = [-1]*(l+1)
        ans = None
        for edge in edges:
        	u,v = edge
        	join = union(u,v, ary)
        	if not join:
        		return [u,v]

eggs = [[1,2], [1,3], [2,3]]
s=Solution()
print(s.findRedundantConnection(eggs))
