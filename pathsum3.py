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
        self.ans = 0
        def findsum(parent, sum):
            if parent is None:
                return 0
            else:
                itersum = findsum(parent.left, sum-parent.val) + findsum(parent.right, sum-parent.val)
                if parent.val == sum:
                    return 1+itersum
                return itersum

        def countsum(parent, sum):
            if parent is None:
                return 0
            else:
                return findsum(parent, sum)+countsum(parent.left, sum)+countsum(parent.right, sum)
        return countsum(root, sum)



