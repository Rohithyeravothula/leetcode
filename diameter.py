class Solution:
    def diameterOfBinaryTree(self, root):
        return self.diameterOfBT(root)[0]
    def diameterOfBT(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None or (root.left is None and root.right is None):
            return (0,0)  # diameter, height
        else:
            left = self.diameterOfBT(root.left)
            right = self.diameterOfBT(root.right)
            height = 1 + max(left[1], right[1])
            diameter = 0
            if root.left is not None:
                diameter = 1+left[1]
            if root.right is not None:
                diameter += 1+right[1]
            diameter = max(diameter, max(left[0], right[0]))
            return (diameter, height)
