# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def get_leaves(root, leaves):
            if not root:
                return None
            if root.left is None and root.right is None:
                leaves.append(root)
            get_leaves(root.left, leaves)
            get_leaves(root.right, leaves)

        root1_leaves = []
        root2_leaves = []
        get_leaves(root1, root1_leaves)
        get_leaves(root2, root2_leaves)
        if root1_leaves == root2_leaves:
            return True
        return False
