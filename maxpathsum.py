# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxvalue = -1*float("inf")
        def pathmax(root):
            if root is None:
                return 0
            else:
                left = max(0, pathmax(root.left))
                right = max(0, pathmax(root.right))
                self.maxvalue = max(left + right + root.val, self.maxvalue)
                return max(left, right)+root.val
        pathmax(root)
        return self.maxvalue
