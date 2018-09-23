# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_max(cur):
            if not cur:
                return -1*float("inf"), -1*float("inf")
            lps, lmax = get_max(cur.left)
            rps, rmax = get_max(cur.right)
            cps = cur.val + max(0, max(lps, rps))
            cmax = max(max(lmax, rmax), max(lps, 0) + max(rps, 0) + cur.val)
            return cps, cmax
        return get_max(root)[1]