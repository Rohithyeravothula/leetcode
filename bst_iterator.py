# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return not self.stack == []
        

    def next(self):
        """
        :rtype: int
        """
        top = self.stack.pop()
        right = top.right
        while right:
            self.stack.append(right)
            right = right.left
        return top.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())