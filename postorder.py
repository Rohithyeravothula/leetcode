# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self)

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        stack = []
        p = root
        while len(stack) != 0 or p is not None:
            if p is not None:
                ans.append(p.val)
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                p = p.right
        return ans



a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.right.left = TreeNode(4)
a.right.left.right = TreeNode(5)


s=Solution()
print(s.postorderTraversal(a))