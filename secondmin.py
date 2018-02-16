# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return -1
        self.min2 = float("inf")
        self.min1 = root.val
        def find_min2(cur):
            if cur is None:
                return None
            else:
                if cur.val > self.min1 and cur.val < self.min2:
                    self.min2=cur.val
                elif cur.val == root.val:
                    find_min2(cur.left)
                    find_min2(cur.right)
        find_min2(root)
        if self.min2 == float("inf"):
            return -1
        return self.min2

s=Solution()
print(s.findSecondMinimumValue(None))