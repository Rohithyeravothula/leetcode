# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        def build(n):
        	if n==0:
        		return []
        	elif n == 1:
        		return [TreeNode(0)]
        	response = []
        	for i in range(1, n, 2):
        		left = build(i)
        		right = build(n-i-1)
        		for t1 in left:
        			for t2 in right:
        				c = TreeNode(0)
        				c.left = t1
        				c.right = t2
        				response.append(c)
        	return response
        return build(N)

s = Solution()
s.allPossibleFBT(0)


