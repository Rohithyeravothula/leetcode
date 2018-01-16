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
        def samepath(root, uval):
        	if root is None:
        		return 0, 0 # max path, incr path
        	else:
        		if root.val == uval:
        			left_path, left_cont_path = samepath(root.left, uval)
        			right_path, right_cont_path = samepath(root.right, uval)
        			return max(max(left_path, right_path), 1+left_cont_path+right_cont_path), 1+max(left_cont_path, right_cont_path)
        		else:
        			left_path, left_cont_path = samepath(root.left, root.val)
        			right_path, right_cont_path = samepath(root.right, root.val)
        			return max(max(left_path, right_path), 1+left_cont_path+right_cont_path), 0
        if root is None:
        	return 0
        ans = samepath(root, root.val)
        return max(ans[0], ans[1])

from graph import *
s=Solution()
t=leetcode_tree([1,2,1,3,4,5,5,1])
print(s.longestUnivaluePath(t))