# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def mindiff(cur):
        	if cur.left is None and cur.right is None:
        		return float("inf"), cur.val
        	elif cur.left is None:
        		return mindiff(cur.right)
        	elif cur.right is None:
        		return mindiff(cur.left)
        	else:
        		leftdiff, leftnode = mindiff(cur.left)
        		rightdiff, rightnode = mindiff(cur.right)
        		diffmin = min(leftdiff, rightdiff)
        		curmin = min(abs(cur.val - cur.left.val), abs(cur.val, rightnode))
        		return min(curmin, diffmin), rightnode

        if root is not None:
        	return mindiff(root)[0]
        return 0