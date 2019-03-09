# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.levels = {}
        def build(cur, n, l):
        	if not cur:
        		return
        	if l not in self.levels:
        		self.levels[l] = [float('inf'), -float('inf')]

        	self.levels[l] = [min(self.levels[l][0], n), max(self.levels[l][1], n)]
        	build(cur.left, 2*n+1, l+1)
        	build(cur.right, 2*n+2, l+1)
        build(root, 0, 0)
        ans = 0
        for (l,r) in self.levels.values():
        	ans = max(ans, 1+r-l)
        return ans

from graph import leetcode_tree
t = leetcode_tree([1,2,3,4,None,None,7,8,None,None,9])
t = leetcode_tree([1])
print(Solution().widthOfBinaryTree(t))


