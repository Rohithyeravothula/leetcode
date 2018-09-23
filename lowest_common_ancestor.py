# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def get_lca(cur, p, q):
            if cur in {None, p, q}:
                return cur

            left = get_lca(cur.left, p, q)
            right = get_lca(cur.right, p, q)
            if left is not None and right is not None:
                return cur
            elif left is not None:
                return left
            return right
        return get_lca(root, p, q)

from graph import *
t = leetcode_tree([3,5,1,6,2,0,8,None,None,7,4])
s = Solution()
print(s.lowestCommonAncestor(t, 5, 1).val)