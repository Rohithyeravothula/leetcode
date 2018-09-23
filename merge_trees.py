class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def merge(ltree, rtree):
            if not ltree and not rtree:
                return None

            elif not ltree:
                return rtree

            elif not rtree:
                return ltree

            ltree.val = ltree.val + rtree.val
            ltree.left = merge(ltree.left, rtree.left)
            ltree.right = merge(ltree.right, rtree.right)
            return ltree
