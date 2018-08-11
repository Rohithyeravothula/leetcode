# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_count(cur):
        	if not cur:
        		return -1
        	if not cur.left and not cur.right:
        		return 0
        	left_val = get_count(cur.left)
        	right_val = get_count(cur.right)
        	if left_val == -1:
        		if cur.val == cur.right.val:
        			cur_ans = right_val + 1
        		return 0 
        	if right_val == -1:
        		if cur.val == cur.left.val:
        			cur_ans = left_val + 1
        		return 0

        	if cur.val == cur.left and cur.left.val == cur.right.val:
        		return left_val + right_val + 2

        	elif cur.val == cur.left:
        		return left_val + 1

        	elif cur.val == cur.right:
        		return right_val + 1

        	else:
        		return 0

        ans = 0
        get_count(root)
        return ans

