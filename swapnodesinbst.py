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
        def print_nodes(a):
            if a is None:
                return None
            else:
                return a.val

        def is_leaf(node):
            if node.left is None and node.right is None:
                return True
            return False

        self.left = None
        self.right = None
        def left_order(cur):
            if cur is None:
                return None
            else:
                left_order(cur.left)
                if self.left is None and self.prev.val >= cur.val:
                    self.left = self.prev

                if self.left is not None and self.prev.val >= cur.val:
                    self.right = cur

                self.prev = cur
                left_order(cur.right)


        self.prev = TreeNode(-1*float("inf"))
        left_order(root)
        self.left.val, self.right.val = self.right.val, self.left.val