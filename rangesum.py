# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def getsum(root, l, r):
        	if not root:
        		return 0

        	cur = root.val if root.val >= l and root.val <= r else 0
        	left = getsum(root.left, l, r) if root.val >= l else 0
        	right = getsum(root.right, l, r) if root.val <= r else 0
        	return cur + left + right
        return getsum(root, L, R)