# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.min = float("inf")
        self.nodes = []
        def inorder(cur):
        	if cur is not None:
        		inorder(cur.left)
        		self.nodes.append(cur.val)
        		inorder(cur.right)

        inorder(root)
        l = len(self.nodes)
        for i in range(1, l):
        	self.min = min(self.min, self.nodes[i] - self.nodes[i-1])
        return self.min

from graph import *
s=Solution()
t  = leetcode_tree([2,None, 3])
print(s.minDiffInBST(t))
