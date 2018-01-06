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
                return 0
            else:
                if sum == cur.val:
                    return 1
                return cursum(cur.left, sum-cur.val) or cursum(cur.right, sum-cur.val)


        self.count = 0
        cursum(root, sum)
        return self.count


