# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def invert(cur):
        	if cur:
        		cur.left, cur.right = cur.right, cur.left
        		invert(cur.left)
        		invert(cur.right)
        invert(root)
        return root

from graph import *
t = leetcode_tree([1,2,3])
s = Solution()
s.invertTree(t)
print(t.left.val)