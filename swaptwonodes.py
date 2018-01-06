# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.inorder = []
        def __inorder(cur):
        	if cur is None:
        		return None
        	else:
        		__inorder(cur.left)
        		self.inorder.append(cur)
        		__inorder(cur.right)
        __inorder(root)
        l = len(self.inorder)
        for i in range(0, l-1):
        	if self.inorder[i].val > self.inorder[i+1].val:
        		break
        for j in range(l-1, i, -1):
        	if self.inorder[j].val < self.inorder[j-1].val:
        		break
        self.inorder[i].val, self.inorder[j].val = self.inorder[j].val, self.inorder[i].val