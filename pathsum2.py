# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def cursum(cur, sum):
        	if cur is None:
        		return []
        	if cur.left is None and cur.right is None:
        		if sum == cur.val:
        			return [[cur.val]]
        		else:
        			return []
        	else:
        		curpath = cursum(cur.left, sum-cur.val) + cursum(cur.right, sum-cur.val)
        		ans = []
        		for path in curpath:
        			ans.append([cur.val] + path)
        		return ans
        return cursum(root, sum)


