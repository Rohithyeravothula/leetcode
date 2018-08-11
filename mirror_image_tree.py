# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(leftnode, rightnode):
            if (leftnode and not rightnode) or (rightnode and not leftnode):
                return False
            if not leftnode and not rightnode:
                return True
            if leftnode.val != rightnode.val:
                return False
            return check(leftnode.left, rightnode.right) and check(leftnode.right, rightnode.left)
        if not root:
            return False
        return check(root.left, root.right)


from graph import *

t = []

s = Solution()
print(s.isSymmetric(leetcode_tree(t)))
