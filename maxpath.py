# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rootpath(cur):
            if cur.left is None and cur.right is None:
                return max(0, cur.val)
            elif cur.left is None:
                return max(cur.val, cur.val+rootpath(cur.right))
            elif cur.right is None:
                return max(cur.val, cur.val+rootpath(cur.left))
            else:
                return cur.val + max(rootpath(cur.left), rootpath(cur.right))

        def pathSum(cur):
            if cur.left is None and cur.right is None:
                return cur.val, max(0, cur.val)
            elif cur.left is None:
                right_path_sum = pathSum(cur.right)
                root_max = max(cur.val, cur.val + rootpath(cur.right))
                return max(right_path_sum, cur.val), root_max
            elif cur.right is None:
                ""
            else:
                left_path_sum = pathSum(cur.left)
                right_path_sum = pathSum(cur.right)
                path_max = max(left_path_sum, right_path_sum)
                cur_root_max = max(cur.val, cur.val + max(left_root_sum, right_root_sum))
                root_max = max(cur.val + left_root_sum + right_root_sum, cur_root_max)
                return path_max, cur_root_max

        return pathSum(root)


