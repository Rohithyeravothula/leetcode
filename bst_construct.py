# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        l = len(nums)
        if l==0:
        	return None
        elif l == 1:
        	return TreeNode(nums[0])
        else:
        	m = l//2
        	cur = TreeNode(nums[m])
        	cur.left = self.sortedArrayToBST(nums[0:m])
        	cur.right = self.sortedArrayToBST(nums[m+1:])
        	return cur

from graph import *
s=Solution()
a=[]
t = s.sortedArrayToBST(a)
print(inorder(t))