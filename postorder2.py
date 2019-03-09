# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        ans = []
        stk = []
        cur = root
        while stk or cur:
        	while cur:
        		stk.append(cur)
        		ans.append(cur.val)
        		cur = cur.right
        	while stk and not cur:
        		cur = stk.pop()
        		cur = cur.left if cur.left else None
        return ans[::-1]