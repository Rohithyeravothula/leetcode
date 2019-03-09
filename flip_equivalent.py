# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def compare(ltree, rtree):
            if not ltree and not rtree:
                return True
            elif (not ltree and rtree) or (not rtree and ltree):
                return False

            if ltree.val == rtree.val:
                c1=compare(ltree.left, rtree.left) and compare(ltree.right, rtree.right)
                c2=compare(ltree.left, rtree.right) and compare(ltree.right, rtree.left)
                return c1 or c2
            return False
        compare(root1, root2)