# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
def extract_left_node(node):
            if node.left and not node.left.left and not node.left.right:
                return node.left
            return None

        def get_sum(cur):
            if not cur:
                return 0
            left = extract_left_node(cur)
            if left:
                return left.val
            return get_sum(cur.left) + get_sum(cur.right)
        return get_sum(root)
"""

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_sum(cur, b):
            if not cur:
                return 0
            if not cur.left and not cur.right:
                return cur.val * b
            return get_sum(cur.left, 1) + get_sum(cur.right,0)
        return get_sum(root, 0)
        