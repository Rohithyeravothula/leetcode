# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        actual=list(range(1, n+1))
        def getTrees(a, cur):
        	l = len(a)
        	trees = []
        	for i in range(0, l):
        		left = getTrees(a[0:i], cur)
        		for lefttree in left:
        			
        		right = getTrees(a[i+1:], cur)
