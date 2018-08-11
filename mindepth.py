# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        cur = [root]
        depth = 1
        while cur:
            newcur = []
            for node in cur:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    newcur.append(node.left)
                if node.right:
                    newcur.append(node.right)
            if not newcur:
                return depth
            cur = newcur
            depth += 1
        return depth


from graph import *


t = [1,2,2,3,4,4,3]
s = Solution()
print(s.minDepth(leetcode_tree(t)))