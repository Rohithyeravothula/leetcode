class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        def delete(current, val):
            if current is None:
                return None
            if val == current.val:
                if current.left is None:
                    return current.right
                if current.right is None:
                    return current.left
                else:
                    minval = current.right.val
                    tmp  = current.right
                    while tmp:
                        minval = tmp.val
                        tmp = tmp.left
                    current.val = minval
                    current.right = delete(current.right, minval)
            elif val < current.val:
                current.left = delete(current.left, val)
            elif val > current.val:
                current.right = delete(current.right, val)
            return current
        
        self.root = delete(root, key)
        return self.root