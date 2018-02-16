# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find(self, root, parent, val):
        if root is None:
            return None, None
        else:
            if root.val == val:
                if root.left is not None and root.left.val == val:
                    return self.find(root.left, root, val)
                elif root.right is not None and root.right.val == val:
                    return self.find(root.right, root, val)
                return root, parent
            elif root.val < val:
                return self.find(root.right, root, val)
            elif root.val > val:
                return self.find(root.left, root, val)

    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if root is None:
            return [None, None]
        cur, parent = self.find(root, None, V)
        # print(cur, parent)
        if parent is None:
            if root.val <= V:
                right = root.right
                root.right = None
                return [root, right]
            else:
                left = root.left
                root.left = None
                return [root, left]
        else:
            if parent.left == cur:
                parent.left = None
            else:
                parent.right = None
            return [root, cur]

from graph import *
bst = leetcode_tree([4,4,4,4])
vv = 1
ss=Solution()
print(ss.splitBST(bst, vv))
# print(ss.find(bst, None, 3))