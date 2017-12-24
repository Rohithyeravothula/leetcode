# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diff = None
        self.prev = None
        def visit_nodes(cur):
        	if cur is None:
        		return None
        	else:
        		visit_nodes(cur.left)
        		if self.prev is None:
        			self.prev = cur.val
        		elif self.diff is None:
        			self.diff = abs(cur.val - self.prev)
        			self.prev = cur.val
        		else:
        			self.diff = min(self.diff, abs(self.prev - cur.val))
        			self.prev = cur.val
        		visit_nodes(cur.right)
        visit_nodes(root)
        return self.diff

        