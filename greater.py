# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convert(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None:
            self.convert(root.right)
            root.val += self.count
            self.count = root.val
            self.convert(root.left)
        return root

    def convertBST(self, root):
        self.count = 0
        return self.convert(root)

s=Solution()
s.convertBST(TreeNode(1))