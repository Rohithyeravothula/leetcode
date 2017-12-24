# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from graph import *

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        l = len(inorder)
        postorder = postorder[::-1]
        self.index=0
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
                cur.right = construct(pre, idx+1, right, inomap)
                cur.left = construct(pre, left, idx, inomap)
                return cur
        return construct(postorder, 0, l, inomap)

post = [3,4,2,6,5,1]
ino = [3,2,4,1,5,6]
s=Solution()
print(inorder(s.buildTree(ino, post)))