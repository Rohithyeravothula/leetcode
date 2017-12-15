# Definition for a binary tree node.
from graph import *

from collections import deque
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def find_node(cur, val):
            if cur is None:
                return None
            elif cur.val == val:
                return cur
            else:
                left = find_node(cur.left, val)
                if left:
                    return left
                right = find_node(cur.right, val)
                if right:
                    return right
                return None
        def closest_leaf(cur, d):
            if cur is None:
                return None
            if cur.left is None and cur.right is None:
                return d, cur
            elif cur.left is None:
                return closest_leaf(cur.right, d+1)
            elif cur.right is None:
                return closest_leaf(cur.left, d+1)
            else:
                left = closest_leaf(cur.left, d+1)
                right = closest_leaf(cur.right, d+1)
                if left[0] < right[0]:
                    return left
                return right

        #u is node, and v is val
        def dist(u, v):
            if u is None:
                return float("inf")
            elif u.val ==v:
                return 0
            else:
                return 1+min(dist(u.left, v), dist(u.right, v))


        if root is None:
            return 0
        node = find_node(root, k)
        ans, ans_node = closest_leaf(node, 0)
        cur = root
        while cur is not None:
            left = find_node(cur.left, k)
            right = find_node(cur.right, k)
            # print(left, right)
            if left is None and right is None:
                break
            check = cur.left
            if right is None:
                check = cur.right
            if check is not None:
                # print("val " + str(check.val)) 
                leaf_dist, leaf_node = closest_leaf(check, 0)
                node_dist = dist(cur, k)
                print(leaf_dist, node_dist, cur.val)
                if leaf_dist+node_dist < ans:
                    ans = leaf_dist+node_dist
                    ans_node = leaf_node
            if left is not None:
                cur = cur.left 
            else:
                cur = cur.right
        return ans_node.val



s=Solution()
print(s.findClosestLeaf(a, 2))