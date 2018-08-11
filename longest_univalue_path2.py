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
                return 0
            left, right = get_count(cur.left), get_count(cur.right)
            left = (left + 1) if cur.left and cur.left.val == cur.val else 0
            right = (right + 1) if cur.right and cur.right.val == cur.val else 0
            self.long = max(self.long, left+right)
            return max(left, right)
        self.long = 0
        get_count(root)
        return self.long

from graph import leetcode_tree
t = leetcode_tree([2,2,3,2,2,4,5,2,3,2])
# t = leetcode_tree([1,1])
# t = leetcode_tree([5,4,5,1,1,5])
s = Solution()
print(s.longestUnivaluePath(t))
