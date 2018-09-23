# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stk = []
        head = root
        result = []
        while stk or head:
            if head:
                while head:
                    stk.append(head)
                    head = head.left
            else:
                head = stk.pop()
                result.append(head.val)
                head = head.right
        return result

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stk = []
        head = root
        result = []
        while stk or head:
            if head:
                while head:
                    result.append(head.val)
                    stk.append(head)
                    head = head.left
            else:
                head = stk.pop()
                head = head.right
        return result
