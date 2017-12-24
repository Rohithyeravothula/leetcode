class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def height(cur):
            if cur is None:
                return 0
            else:
                return 1+height(cur.left)

        def nodes(cur):
            if cur is None:
                return 0
            h = height(cur)
            hr = height(cur.right)
            if hr == h:
                return (1 << h) + nodes(cur.right)
            else:
                return (1 << hr) + nodes(cur.left)
        return nodes(root)