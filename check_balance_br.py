# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(cur):
            if not cur:
                return 0, True
            lh, lv = check(cur.left)
            rh, rv = check(cur.right)
            if not (lv and rv):
                return 0, False
            if lv and rv and abs(lh-rh) <= 1:
                return max(lh, rh)+1, True
            return 0, False
                
        