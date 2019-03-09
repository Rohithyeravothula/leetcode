# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
from graph import *

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        def build(cur, val):
            if not cur:
                return TreeNode(val)
            if cur.val < val:
                t = TreeNode(val)
                t.left = cur
                return t
            cur.right = build(cur.right, val)
            return cur
        return build(root, val)

inp, val = [5,2,4,null,1], 3
inp, val = [],1
inp, val = [5,2,3,null,1], 6
t = leetcode_tree(inp)
ut = Solution().insertIntoMaxTree(t, val)
print(inorder(ut))
