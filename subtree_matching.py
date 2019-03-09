class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def preorder(cur):
            if not cur:
                return '#'
            return "*" + str(cur.val) + preorder(cur.left) + preorder(cur.right)
        return preorder(t) in preorder(s)





