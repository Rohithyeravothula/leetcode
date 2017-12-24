# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def robherlper(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0,0 # [cur, children]
        else:
            left, leftchild = self.robherlper(root.left)
            right, rightchild = self.robherlper(root.right)
            return max(left+right, root.val + leftchild+rightchild), left+right 
    def rob(self, root):
        return self.robherlper(root)[0]
