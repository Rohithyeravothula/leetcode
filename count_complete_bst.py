# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_height(head):
        	cur = head
        	count = 0
        	while cur:
        		count += 1
        		cur = cur.left
        	return count

        def count(head):
        	if not head:
        		return 0
        	if not head.left and not head.right:
        		return 1
        	left = get_height(cur.left)
        	right = get_height(cur.right)
        	if left == right:
        		return 2**(left+1) + count(cur.right)
        	return 2**(right+1) + count(cur.left)
        return count(root)
