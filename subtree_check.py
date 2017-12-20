# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def check_tree(self, left_tree, right_tree):
        if left_tree is None and right_tree is None:
            return True
        elif left_tree is None or right_tree is None:
            return False
        else:
            if left_tree.val == right_tree.val:
                return self.check_tree(left_tree.left, right_tree.left) and self.check_tree(left_tree.right, right_tree.right)
            return False

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None and t is None:
            return True
        elif t is None:
            return True
        elif s is None:
            return False
        elif s.val == t.val and self.check_tree(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


        