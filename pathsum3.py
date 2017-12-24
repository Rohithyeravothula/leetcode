# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countSum(root, target):
        if root is None:
            return 0
        else:
            if target == root.val:
                self.count += 1
            self.countSum(root.left, target)
            self.countSum(root.left, target-root.val)
            self.countSum(root.right, target)
            self.countSum(root.right, target-root.val)
            if root.left is not None:
                self.countSum(root.left, target-root.val-root.left.val)
            if root.right is not None:
                self.countSum(root.right, target-root.val-root.right.val)
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count = 0
        self.countSum(root, sum)
        return self.count
