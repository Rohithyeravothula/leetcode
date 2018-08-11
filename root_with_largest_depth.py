# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def max_depth(cur):
            if not cur:
                return 0, 0

            left_node, left_depth = max_depth(cur.left)
            right_node, right_depth = max_depth(cur.right)
            if left_depth == right_depth:
                return cur, 1+left_depth
            elif left_depth > right_depth:
                return left_node, 1+left_depth
            return right_node, 1+right_depth

        if not root:
            return root
        node, depth = max_depth(root)
        return node

from graph import leetcode_tree
g = [3,5,1,6,2,0,8,None,None,7,4]
g = [1,2,3,4,5]
t = leetcode_tree(g)
s = Solution()
ans = s.subtreeWithAllDeepest(t)

print(ans.val) if ans else print("none tyupe")

