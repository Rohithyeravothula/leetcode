# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None
        elif t1 is None:
            cur = TreeNode(t2.val)
            cur.left = self.mergeTrees(t1, t2.left)
            cur.right = self.mergeTrees(t1, t2.right)
            return cur
        elif t2 is None:
            cur = TreeNode(t1.val)
            cur.left = self.mergeTrees(t1.left, t2)
            cur.right = self.mergeTrees(t1.right, t2)
            return cur
        else:
            cur = TreeNode(t1.val + t2.val)
            cur.left = self.mergeTrees(t1.left, t2.left)
            cur.right = self.mergeTrees(t1.right, t2.right)
            return cur
        