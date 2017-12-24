# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from graph import *

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.index=0
        l = len(inorder)
        inomap = {}
        for idx, val in enumerate(inorder):
            inomap[val] = idx

        def construct(pre, left, right, inomap):
            print(left, right, self.index)
            if left == right-1:
                self.index += 1
                return TreeNode(inorder[left])
            elif left == right:
                return None
            else:
                idx = inomap[pre[self.index]]
                cur = TreeNode(pre[self.index])
                self.index += 1
                cur.left = construct(pre, left, idx, inomap)
                cur.right = construct(pre, idx+1, right, inomap)
                return cur
        return construct(preorder, 0, l, inomap)

pre=[1,2,3,4,5,6]
ino=[3,2,4,1,5,6]
# pre=[1,2,3,4]
# ino=[2,1,3,4]
s=Solution()
print(inorder(s.buildTree(pre, ino)))