# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
        def build(cur):
        	if not cur:
        		return None, None
        	left_head, left_tail = build(cur.left)
        	right_head, right_tail = buid(cur.right)
        	if not left_head:
        		left_head, left_tail = right_head, right_tail
        		right_head = None

        	if not left_head:
        		return cur, cur

        	cur.left = None
        	cur.right = left_head
        	left_tail.right = right_head
        	if not right_tail:
        		right_tail = left_tail
        	return cur, right_tail
"""
class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def get_inorder(cur, ino):
        	if cur:
        		get_inorder(cur.left, ino)
        		ino.append(cur.val)
        		get_inorder(cur.right, ino)

        inorder = []
        get_inorder(root, inorder)
        head = TreeNode(-1)
        cur = head
        for val in inorder:
        	cur.right = TreeNode(val)
        	cur = cur.right
        return head.next



